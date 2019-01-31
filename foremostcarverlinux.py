import subprocess # importeer subprocess zodat er linux tools aangeroepen kunnen worden
import defaultlogger
import apt # importeer de apt library zodat de linux package library gelezen kan worden

def foremostapt(): # maak een def aan om te controleren of Foremost al op het apparaat staat
    cache = apt.Cache() # definiëer de apt cache
    cache.open() # open de cache om deze uit te lezen
    try: # probeer om te kijken of Foremost is geïnstalleerd
        cache['foremost'].is_installed
        defaultlogger.logging.info("Foremost is aangetroffen op het apparaat.")  # log dit
        print("Foremost is gevonden op dit apparaat.") # meld dit
    except KeyError: # vang de error die cache gooit als Foremost niet gevonden is af
        print("Foremost is niet gevonden op dit apparaat.") # meld dit
        print("Foremost is benodigd om te carven en wordt nu geïnstalleerd.")
        subprocess.call(["sudo", "apt-get", "update"]) # update de package lijst
        subprocess.call(["sudo", "apt-get", "install", "foremost"]) # installeer foremost
        defaultlogger.logging.info("Foremost is niet aangetroffen op dit apparaat en werd geïnstalleerd.")  # log dit

def carve(evidenceid,image): # maak een def aan om te carven
    foremostapt() # voer de def foremostapt uit om te controleren of foremost geïnstalleerd is
    try:
        crv = subprocess.call(["foremost","-t","all","-o","output" + evidenceid, "-i", image]) # voer met subprocess het carven uit met foremost
        return crv # geef het product van het carven door
    except(): # vang foutmeldingen van foremost af
        print("Het carven is niet gelukt.") # meld het mislukken van het carven
        recarve = input(str("Druk op enter op opnieuw te carven. Druk op iets anders om door te gaan.")) # geef de optie op opnieuw te carven
        if recarve = "": # als er op enter wordt gedrukt
            carve(evidenceid,image) # carve opnieuw