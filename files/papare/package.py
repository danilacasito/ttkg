# TTKG "package" INSTALL file
import os
os.system("mkdir -pv /usr/app/papare")
with open("/usr/app/papare/papare") as f:
    f.write("#!/usr/bin/python3")
    f.write("print('Hello World By Papare')")
e = os.system("ln -sv /usr/app/papare/papare /usr/bin/papare")
if not e == 0:
    print("Program returned with code "+str(e))
    exit(e)
else:
    exit(0)
