import os
import time

try:
	import requests
	from colorama import init, Fore, Style

except ModuleNotFoundError:
	print("Installing missing module(s)\n")
	os.system("pip install requests colorama")
	import requests
	from colorama import init, Fore, Style

init()

print(Style.BRIGHT + Fore.RED + "  _  __                 _             \n | |/ /                | |            \n | ' / _ __ _   _ _ __ | | _____ _ __ \n |  < | '__| | | | '_ \| |/ / _ \ '__|\n | . \| |  | |_| | | | |   <  __/ |   \n |_|\_\_|   \__,_|_| |_|_|\_\___|_|   \n" + 
	  Fore.MAGENTA + "="*38, end="\n")

while True:
	print(Fore.RED + '\nEnter the CSS link\n>>> ' + Fore.GREEN, end="")
	
	try:
		css = requests.get(input()).text
	
	except Exception:
		print(Fore.CYAN + "Enter a valid link!" + Fore.RED)
	
	else:
		print(Fore.CYAN + "\nIs it for [ENTER 1 or 2]:\n\t[1] In-Game\n\t[2] Hub\n\t>>> " + Fore.RED, end="")
		if (input().strip()) in ["", "1"]:
			t="main_custom"
		
		else:
			t="social_custom"
		
		break

if (name:="MyResourceSwapper") not in os.listdir():
	os.makedirs(f"{name}/css")
	with open(f"{name}/css/{t}.css", "w") as f:
		f.write(css)
		time.sleep(2)
		print(Fore.MAGENTA + "\nSuccessfully imported the CSS!")
	
	for k, v in {"init.js":'let request=chrome.webRequest.onBeforeRequest;function searchDir(e,r){for(let t of r)e.getDirectory(t.name,{create:!1},e=>{e.createReader().readEntries(r=>{let t=r.filter(e=>e.isDirectory),i=r.filter(e=>e.isFile);t.length&&searchDir(e,t);for(let e of i)request.addListener(r=>({redirectUrl:chrome.extension.getURL(e.fullPath.replace("/crxfs/",""))}),{urls:["*://*.krunker.io/"+e.fullPath.replace("/crxfs/","")+"*"]},["blocking"])})})}chrome.runtime.getPackageDirectoryEntry(e=>{e.createReader().readEntries(r=>{searchDir(e,r.filter(e=>!["init.js","manifest.json","README.md","LICENSE",".git"].includes(e.name)))})});',"manifest.json":'{"name":"Custom Krunker CSS","version":"0.0.1","manifest_version":2,"description":"https://krunker.io","permissions":["webRequest","webRequestBlocking","*://*.krunker.io/*","http://127.0.0.1:8080/*"],"web_accessible_resources":["*.obj","*.png","*.mp3","*.css","*.json","*.ttf","*.otf","*.ico","*.svg","*.txt"],"background":{"scripts":["init.js"]}}'}.items():
		with open(f"{name}/{k}", "w") as f:
			f.write(v)
			time.sleep(3)
			print(Fore.CYAN + f"Created {k}")
	
	print(Fore.MAGENTA + "\nSteps to load the extension:\n" + Fore.RED + 
			"[1] Go to your browser’s extensions page and enable *Developer mode*\n    on top-right corner." + 
			f"\n[2] Drag and drop down the folder *{name}* to the page." + 
			"\n[3] https://krunker.io :D")
	
else:
	with open(f"{name}/css/{t}.css", "w") as f:
		f.write(css)
		time.sleep(2)
		print(Fore.MAGENTA + "\nSuccessfully imported the CSS!\n")
		print(Fore.CYAN + "You may have to reload the extension")

print(Fore.GREEN + "\nPress ENTER to exit.")
input()
