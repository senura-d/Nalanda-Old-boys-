import os

# Favicon tag for pages in root (Home.html)
ROOT_FAVICON = '<link rel="icon" type="image/png" href="img/Logo_of_Nalanda_College_Colombo.png">'
# Favicon tag for pages in /screens/ (one level deeper)
SCREEN_FAVICON = '<link rel="icon" type="image/png" href="../img/Logo_of_Nalanda_College_Colombo.png">'

screens_dir = r'c:\Users\user\Desktop\nalanda oldboy website ui\screens'
home        = r'c:\Users\user\Desktop\nalanda oldboy website ui\Home.html'

def inject_favicon(filepath, favicon_tag):
    with open(filepath, encoding='utf-8') as fh:
        content = fh.read()

    # Skip if favicon already present
    if 'rel="icon"' in content:
        # Replace existing favicon href
        import re
        new_content = re.sub(r'<link[^>]+rel="icon"[^>]*>', favicon_tag, content)
    else:
        # Insert after <head> or after first <meta charset
        if '<meta charset' in content:
            new_content = content.replace('<meta charset', favicon_tag + '\n<meta charset', 1)
        else:
            new_content = content.replace('<head>', '<head>\n' + favicon_tag, 1)

    with open(filepath, 'w', encoding='utf-8') as fh:
        fh.write(new_content)
    print(f'[DONE] {os.path.basename(filepath)}')

# Home.html (root level)
inject_favicon(home, ROOT_FAVICON)

# All screens/*.html
for fname in os.listdir(screens_dir):
    if fname.endswith('.html'):
        inject_favicon(os.path.join(screens_dir, fname), SCREEN_FAVICON)
