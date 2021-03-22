import os
import sys
from time import sleep
import requests
time = 0
print("-- YOU MUST OPEN THIS AS ADMIN, IF YOU RUNNED THIS AS ADMIN WAIT 5 SECONDS, IF YOU RUNNED AS NON-ADMIN, PLEASE DO CTRL+C and RUN THIS AS ADMINISTRATOR")
sleep(5)
os.system("mkdir temp")
os.chdir("temp")
if sys.argv[1]:
    if sys.argv[1] == "install":
        if sys.argv[2]:
            print("Downloading "+sys.argv[2]+"...")
            r = request.get("https://raw.githubusercontent.com/danilacasito/ttkg/programs/files/"+sys.argv[2]+"/package.py")
            with open("package.py", "wb") as f:
                f.write(r.content)
            import package as pkg
            pkg.configure()
            pkg.build()
            pkg.install()
        else:
            print("""
            Usage:
            ttkg install [package]
            python3 ttkg.py install [package] (using source file)
            """)

