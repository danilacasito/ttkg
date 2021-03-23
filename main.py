import os

import sys
from time import sleep
import requests as request
time = 0
a = 0
a = a - 1
for i in sys.argv:
    a = a + 1
print( "There are " + str( a ) + "Arguments" )
print("-- YOU MUST OPEN THIS AS ADMIN, IF YOU RUNNED THIS AS ADMIN WAIT 5 SECONDS, IF YOU RUNNED AS NON-ADMIN, PLEASE DO CTRL+C and RUN THIS AS ADMINISTRATOR")
sleep(5)
os.system("mkdir temp")
os.chdir("temp")
if a > 0:
    if sys.argv[1]:
        if sys.argv[1] == "install":
            if a == 2:
                print("Downloading "+sys.argv[2]+"...")
                r = request.get("https://raw.githubusercontent.com/danilacasito/ttkg/programs/files/"+sys.argv[2]+"/package.py")
                with open("package.py", "wb") as f:
                    f.write(r.content)
                os.system("python3 package.py")
            else:
                print("""
                Usage:
                ttkg install [package]
                python3 ttkg.py install [package] (using source file)
                """)

os.chdir("..")
os.system("rm -rvf temp")
