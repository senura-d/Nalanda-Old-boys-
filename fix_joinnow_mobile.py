import os, re

# Join Now button - make it compact on mobile, full on desktop
# Replace the full-size class string with responsive classes
OLD_JOIN = 'class="bg-primary text-on-primary px-5 py-2 rounded-lg font-bold hover:brightness-110 transition-all shadow-md text-center no-underline"'
NEW_JOIN = 'class="bg-primary text-on-primary px-3 py-1.5 md:px-5 md:py-2 rounded-lg font-bold hover:brightness-110 transition-all shadow-md text-center no-underline text-sm md:text-base"'

screens_dir = r'c:\Users\user\Desktop\nalanda oldboy website ui\screens'
home      = r'c:\Users\user\Desktop\nalanda oldboy website ui\Home.html'
files     = [home] + [os.path.join(screens_dir, f) for f in os.listdir(screens_dir) if f.endswith('.html')]

for filepath in files:
    with open(filepath, encoding='utf-8') as fh:
        content = fh.read()

    if OLD_JOIN not in content:
        print(f'[SKIP] {os.path.basename(filepath)} — pattern not found')
        continue

    new_content = content.replace(OLD_JOIN, NEW_JOIN)
    with open(filepath, 'w', encoding='utf-8') as fh:
        fh.write(new_content)
    print(f'[DONE] {os.path.basename(filepath)}')
