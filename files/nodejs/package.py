import time
import os
import platform
det = platform.system()
def log(text):
    print("[ "+time.asctime()+" ] "+text)
def start():
    log("Downloading NODE.js version 15.12.0")
    os.system("wget https://nodejs.org/dist/v15.12.0/node-v15.12.0.tar.gz > log")
    log("Creating Temporal folder")
    os.system("mkdir temp")
    log("Moving node package to temporaly folder")
    os.system("mv node-v15.12.0.tar.gz temp/nodejs.tar.gz")
    log("Entering temporal folder")
    os.chdir("temp")
    log("Unpacking node.js")
    os.system("tar -xf nodejs.tar.gz")


if det == "Windows":
    print("Lo sentimos, pero Windows no esta soportado por este scipt aún, pero es posible que pueda estarlo")
elif det == "Darwin":
    print("Este script esta diseñado para linux, pero es quizas de que soporte Mac OS por ser de tipo UNIX, este script podría dañar su sistema")
    print("en este caso es mejor que instale NODE.JS desde su pagina web oficial")
    print("Desea continuar?")
    e = input("[y:N]: ")
    if e == "y":
        start()
    else:
        exit(1)
elif det == "Linux":
    print("Instalando NODE.JS")
    start()

