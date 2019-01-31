# deze klasse dient om alle mogelijke inputs af te handelen, en controleert alle variabelen die hierbij aangemaakt worden

import defaultlogger  # importeer de default_logger apart; deze klasse handelt al het loggen af
import os  # importeer os zodat er dingen gedaan kunnen worden met het systeem wat gedraait wordt
import sys  # importeer sys; dit wordt gebruikt voor sys.exit om de tool af te sluiten
import platform  # importeer platform zodat het operating system herkend kan worden dmv platform.system()

def evidenceid_input():  # deze def maakt het evidence id aan en logt dit meteen weg
    evidenceid = input(str("Voer het evidence ID van de USB-stick in. "))
    defaultlogger.loggerconfig(evidenceid)  # maakt een logger object aan
    defaultlogger.logging.info("Evidence ID " + evidenceid + " is ingevoerd en de tool is gestart.")  # logt het inputten van het evidence id
    return evidenceid  # return evidenceid zodat dit gebruikt kan worden in andere functies


def detectos():  # deze def detecteert welk OS er gebruikt wordt
    ostype = platform.system() # maak een variabele van het ostype; deze wordt bepaald door de functie platform.system
    if ostype == "Windows": # als het ostype Windows is:
        defaultlogger.logging.info("Het OS waar de tool op gedraait wordt is Windows.")  # log dit
        return ostype # geef dit door aan het aanroepende script
    if ostype == "Linux": # als het ostype Linux is:
        defaultlogger.logging.info("Het OS waar de tool op gedraait wordt is Linux.")  # log dit
        return ostype # geef dit door aan het aanroepende script


def carve_input():  # creeër een def om de input voor het te carven bestand af te handelen
    cfilename = input("Voer alstublieft de locatie van uw image in. ")  # vraag om de locatie van het carve bestand
    if os.path.isfile(cfilename):  # controleer of de input ook daadwerkelijk een bestand is
        print("Je hebt de image " + cfilename + " gekozen. Voer Y in als dit klopt.")  # vraag om bevestiging
        confirm_choice = str(
            input(""))  # maak van de bevestiging een variabele zodat hier dingen mee gedaan kunnen worden
        if confirm_choice == "Y" or confirm_choice == "y":
            defaultlogger.logging.info("De image " + cfilename + " is gekozen om te carven.")
            return cfilename  # als de bevestiging positief is: return cfilename
        elif confirm_choice == "exit":  # exit routine
            defaultlogger.logging.info("De tool werd voortijdig afgesloten.")
            sys.exit()
        else:
            carve_input()  # als de bevestiging iets anders is dan Y or y, start opnieuw met de input
    else:
        print("Voer alstublieft een geldige bestandslocatie in.")
        carve_input()  # start opnieuw met de input als er geen geldig bestand is ingevoerd


def image_input_station():  # maak een def aan om het usb-station van de te imagen usb-stick in te voeren
    ifile = input(str("Voer alstublieft de locatie van de USB stick in. Druk op enter als u het niet zeker weet. Als dit niet werkt, gebruik fdisk -l. "))
    if ifile == "": # maak een variabele van ifile met invoer; als er op enter gedrukt wordt:
        ifile = "/dev/sdb1" # gebruik dan standaard /dev/sdb1
    defaultlogger.logging.info("Het USB-station " + ifile + " werd geimaged.")  # log het imagen
    return ifile # geef ifile door aan het aanroepende script
