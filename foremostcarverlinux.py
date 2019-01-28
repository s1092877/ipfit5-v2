import subprocess
import toolinputs
import defaultlogger
import apt

def foremostapt():
    cache = apt.Cache()
    cache.open()
    try:
        cache['foremost'].is_installed
        print("Foremost is gevonden op dit apparaat.")
    except KeyError:
        print("Foremost is niet gevonden op dit apparaat.")
        print("Foremost is benodigd om te carven en wordt nu geïnstalleerd.")
        subprocess.call(["sudo", "apt-get", "update"])
        subprocess.call(["sudo", "apt-get", "install", "foremost"])

def carve(evidenceid,image):
    foremostapt()
    try:
        crv = subprocess.call(["foremost","-t","all","-o","output" + evidenceid, "-i", image]) #je moet invullen images/imageX.raw
        return crv
    except():
        print("Carven mislukt")