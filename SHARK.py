import requests
import os
import time
import re
from ConsoleStuff import *
import io


#IM SORRY TO EVERYONE READING THIS, THE CODE IS A ABSOLUTE DUMPSTER FIRE I KNOW BUT IT WORKS, EVEN I STRUGGLE TO EDIT IT. THIS PROJECT WAS STARTED AT 3 AM SO THE BASE IS HORRIBLE SH

if __name__ == '__main__':
	s = requests.session()
	s.headers.update({'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
	Startup()
	target = input("Target site(ex: https://www.google.com): ")
	
	if not "http" in target:
		ishttp = input("Does the host have ssl in place?(y/n): ")

		if "n" in ishttp:
			target = "http://" + target 
		else:
			target = "https://" + target 

	try:
		response = s.get(target, allow_redirects=True)
	except:
		logger.error(f"Site is unreachable check if host is down or misspelled")
		exit(0)

	if not target[-1] == "/":
		target = target + "/"


	basehtml = response.text

	#basedir = target.replace(target.split('/')[-1],"")

	http = target.split("//")[0]
	basedir = http + "//" + target.split('//')[1].split('/')[0]
	#print(f"{basedir} {basedir1}")

	dependancies = list(set([x.group() for x in re.finditer(r'((https?:\/\/(?:www\.|(?!www))){0,1}|\/)(([-a-zA-Z0-9@:%._~#=]{1,256}\/){0,300})[-a-zA-Z0-9@:%._~#=]{1,256}(.js|.png|.css|.jpg|.gif|.html|.xml|.py|.bin|.csv|.htm|.jpeg|.json|.mpeg|.php|.ppt|.pdf|.7z|.svg|.ico|.woff)', basehtml)]))
	
	for dep in dependancies:

		dep = dep.replace('\n','')

		if not "." in dep:
			dependancies.remove(dep)


		elif not "http" in dep:
			dependancies[dependancies.index(dep)] = basedir + dep


	currentprojectfilename = basedir.replace(basedir.split('//')[0], "").replace("/","").replace('.',"-")
	#print(currentprojectfilename)
			
	logger.info(f"Got {len(dependancies)} additional files, making folder {currentprojectfilename}...")

	try:
		os.mkdir(currentprojectfilename)
	except:
		pass

	for dep in dependancies:
		#print(dep)
		if basedir in dep:
			#os.mkdir(currentprojectfilename + "/" + dep.replace(basedir,""))

			clean_dir = dep.replace(basedir,"").replace("//","/")

			#actual useful shit lol
			filename = clean_dir.split('/')[-1]
			dirs = clean_dir.replace(filename,"")
			#print(dirs)
			#print(dep)

			os.makedirs("sites/" + currentprojectfilename + "/" + dirs, exist_ok=True)
			try:
				r = s.get(dep,stream=True)
			except:
				logger.error(f"Failed to get file {filename} Connection refused by server")
				continue
			if r.status_code == 200:
				try:
					with io.open("sites/" + currentprojectfilename + "/" + clean_dir, "wb") as f:
						for chunk in r:
							try:
								f.write(chunk)
							except:
								pass
					logger.info(f"Made file {filename}")
				except:
					logger.error(f"Failed to write file, error")
			else:
				logger.error(f"Failed to get file {filename} http status code {str(r.status_code)}")

			#print(clean_dir)
			#basehtml = basehtml.replace(clean_dir, "./"+ clean_dir)

	basehtml = basehtml.replace("\"/","\"./")
	f = open(currentprojectfilename + "/index.html", "w", encoding="utf-8")
	f.write(basehtml)
	f.close()








