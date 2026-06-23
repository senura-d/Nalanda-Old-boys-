import os, re

# Updated mobile menu script — filters out any "Join Now" links from dropdown
OLD_SCRIPT = """(function(){
  var btn=document.getElementById("menuBtn");
  var menu=document.getElementById("mobileMenu");
  if(!btn||!menu){return;}
  var icon=btn.querySelector(".material-symbols-outlined");
  var desk=document.querySelector("header nav[class*='md:flex']");
  if(desk){
    menu.innerHTML=desk.innerHTML;
    menu.querySelectorAll("a").forEach(function(a){
      a.classList.add("block","py-2");
      a.addEventListener("click",function(){ menu.classList.add("hidden"); if(icon){icon.textContent="menu";} });
    });
  }
  btn.addEventListener("click",function(e){
    e.preventDefault();
    var open=menu.classList.toggle("hidden")===false;
    if(icon){icon.textContent=open?"close":"menu";}
  });
})();"""

NEW_SCRIPT = """(function(){
  var btn=document.getElementById("menuBtn");
  var menu=document.getElementById("mobileMenu");
  if(!btn||!menu){return;}
  var icon=btn.querySelector(".material-symbols-outlined");
  var desk=document.querySelector("header nav[class*='md:flex']");
  if(desk){
    menu.innerHTML=desk.innerHTML;
    // Remove any Join Now button from mobile dropdown
    menu.querySelectorAll("a").forEach(function(a){
      if(a.textContent.trim()==="Join Now"){a.remove();return;}
      a.classList.add("block","py-2");
      a.addEventListener("click",function(){ menu.classList.add("hidden"); if(icon){icon.textContent="menu";} });
    });
  }
  btn.addEventListener("click",function(e){
    e.preventDefault();
    var open=menu.classList.toggle("hidden")===false;
    if(icon){icon.textContent=open?"close":"menu";}
  });
})();"""

screens_dir = r'c:\Users\user\Desktop\nalanda oldboy website ui\screens'
home      = r'c:\Users\user\Desktop\nalanda oldboy website ui\Home.html'
files     = [home] + [os.path.join(screens_dir, f) for f in os.listdir(screens_dir) if f.endswith('.html')]

for filepath in files:
    with open(filepath, encoding='utf-8') as fh:
        content = fh.read()

    if OLD_SCRIPT not in content:
        print(f'[SKIP] {os.path.basename(filepath)} — script pattern not found')
        continue

    new_content = content.replace(OLD_SCRIPT, NEW_SCRIPT)
    with open(filepath, 'w', encoding='utf-8') as fh:
        fh.write(new_content)
    print(f'[DONE] {os.path.basename(filepath)}')
