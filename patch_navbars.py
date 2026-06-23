import os
import re

# Configuration for links
# Key is the label in the navbar (case-insensitive)
routes = {
    "home": "Home.html",
    "about": "about_us.html",
    "membership": "membership.html",
    "events": "events.html",
    "charity": "charity.html",
    "gallery": "gallery.html"
}

def patch_file(filepath, is_root):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the navbar block: <nav class="hidden md:flex gap-8 items-center">...</nav>
    # We use regex to find this block and replace the hrefs inside it
    pattern = re.compile(r'(<nav class="hidden md:flex gap-8 items-center">)(.*?)(</nav>)', re.DOTALL)
    
    def replace_navbar(match):
        start = match.group(1)
        nav_content = match.group(2)
        end = match.group(3)
        
        # Replace individual links in nav_content
        # e.g., <a ... href="#">Home</a> -> href="index.html" or "../index.html"
        link_pattern = re.compile(r'(<a\s+[^>]*?href=")([^"]*)("[^>]*?>)([^<]+)(</a>)', re.DOTALL)
        
        def replace_link(link_match):
            prefix = link_match.group(1)
            old_href = link_match.group(2)
            suffix = link_match.group(3)
            label = link_match.group(4).strip().lower()
            closing = link_match.group(5)
            
            # Decide the correct target file name
            target = ""
            if label == "home":
                target = "Home.html" if is_root else "../Home.html"
            elif label in routes:
                target = routes[label]
                if is_root:
                    target = f"screens/{target}"
            else:
                target = old_href # keep original if unknown label
                
            return f"{prefix}{target}{suffix}{link_match.group(4)}{closing}"
            
        new_nav_content = link_pattern.sub(replace_link, nav_content)
        return f"{start}{new_nav_content}{end}"

    new_content = pattern.sub(replace_navbar, content)
    
    # Also patch any header logo links or "Join Now" or top-level "Home" breadcrumb links if applicable
    # e.g. <a class="..." href="#">Home</a> outside navbar
    # But let's keep it simple and just patch the navbar for now.
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched {filepath}")
    else:
        print(f"No changes made to {filepath}")

# Patch Home.html in root
patch_file("Home.html", is_root=True)

# Patch all html files in screens directory
screens_dir = "screens"
for filename in os.listdir(screens_dir):
    if filename.endswith(".html"):
        patch_file(os.path.join(screens_dir, filename), is_root=False)
