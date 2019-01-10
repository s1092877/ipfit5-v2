#deze klasse dient om alle mogelijke inputs af te handelen, en controleert alle variabelen die hierbij aangemaakt worden

import defaultlogger #importeer de default_logger apart; deze klasse handelt al het loggen af
import os
import sys
import platform

 # maakt evidenceid als global aan zodat deze ook in andere klasses gebruikt kan worden.

def evidenceid_input(): #deze def maakt het evidence id aan en logt dit meteen weg
    evidenceid = input(str("Voer het evidence ID van de USB-stick in. "))
    defaultlogger.loggerconfig(evidenceid) #maakt een logger object aan
    defaultlogger.logging.info("Evidence ID " + evidenceid + " is ingevoerd en de tool is gestart.") #logt het inputten van het evidence id
    return evidenceid #return evidenceid zodat dit gebruikt kan worden in andere functies

def detectos():
    ostype = platform.system()
    if ostype == "Windows":
        print("windows")
        return ostype
    if ostype == "Linux":
        print("linux")
        return ostype

## def os_choice_input(): #deze def onthoudt de keuze voor welk platform de tool uitgevoerdt wordt
##    print("Operating systems:")
##    print("1. Windows") #print een lijst van mogelijke operating systems
##    print("2. Ubuntu")
##    print("3. Raspbian")
##    print("4. Exit")
##    try: #maak een try aan; als int(input) geen int krijgt, gooit int een ValueError
##        os_choice = int(input("Voer hier uw gekozen optie in. ")) #vraag om gekozen OS
##        while not(os_choice == 1 or os_choice == 2 or os_choice == 3 or os_choice == 4): #controleer of os_choice wel één van de bovenstaande opties is
##            print("Kies alstublieft één van de bovenstaande opties.") #vraag om correcte optie
##            os_choice_input()
##        if os_choice == 1: #maak een string aan voor het gekozen OS, voor de log en andere mogelijke zaken waarbij de volledige naam noodzakelijk is
##            os_choice_verbose = str("Windows")
##        elif os_choice == 2:
##            os_choice_verbose = str("Ubuntu")
##        elif os_choice == 3:
##            os_choice_verbose = str("Raspbian")
##        elif os_choice == 4:
##            defaultlogger.logging.info("De tool werd voortijdig afgesloten.")
##            sys.exit()
##        defaultlogger.logging.info("Het OS " + os_choice_verbose + " is gekozen.")  # maak een log entry aan voor de OS keuze
##        return os_choice #passeer os_choice naar main.py als os_selection zodat deze ook in de main gebruikt kan worden
##    except ValueError: #vang value error af
##        print("Voer alstublieft een getal in.")
##        return os_choice_input() #keer terug naar os_choice

def carve_input(): #creeër een def om de input voor het te carven bestand af te handelen
    cfilename = input("Voer alstublieft de locatie van uw image in. ") #vraag om de locatie van het carve bestand
    if os.path.isfile(cfilename): #controleer of de input ook daadwerkelijk een bestand is
        print("Je hebt de image " + cfilename + " gekozen. Voer Y in als dit klopt.") #vraag om bevestiging
        confirm_choice = str(input("")) #maak van de bevestiging een variabele zodat hier dingen mee gedaan kunnen worden
        if confirm_choice == "Y" or confirm_choice == "y":
            defaultlogger.logging.info("De image " + cfilename + " is gekozen om te carven.")
            return cfilename #als de bevestiging positief is: return cfilename
        elif confirm_choice == "exit": #exit routine
            defaultlogger.logging.info("De tool werd voortijdig afgesloten.")
            sys.exit()
        else:
            carve_input() #als de bevestiging iets anders is dan Y or y, start opnieuw met de input
    else:
        print("Voer alstublieft een geldige bestandslocatie in.")
        carve_input() #start opnieuw met de input als er geen geldig bestand is ingevoerd
        
def image_input_station(): #maak een def aan om het usb-station van de te imagen usb-stick in te voeren
    ifile = input(str("Voer alstublieft de locatie van de USB stick in. "))
    return ifile


def image_input_blocksize():
    bsize = input(str(("voer de blocksize in: ")))
    return bsize