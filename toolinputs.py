#deze klasse dient om alle mogelijke inputs af te handelen, en controleert alle variabelen die hierbij aangemaakt worden

import defaultlogger #importeer de default_logger apart; deze klasse handelt al het loggen af

 # maakt evidenceid als global aan zodat deze ook in andere klasses gebruikt kan worden.

def evidenceid_input(): #deze def maakt het evidence id aan en logt dit meteen weg
    evidenceid = input(str("Voer het evidence ID van de USB-stick in. "))
    defaultlogger.loggerconfig(evidenceid)
    defaultlogger.logging.info("Evidence ID " + evidenceid + " is ingevoerd en de tool is gestart.")
    return evidenceid

def os_choice_input(): #deze def onthoudt de keuze voor welk platform de tool uitgevoerdt wordt
    print("1. Windows") #print een lijst van mogelijke operating systems
    print("2. Ubuntu")
    print("3. Raspbian")
    try: #maak een try aan; als int(input) geen int krijgt, gooit int een ValueError
        os_choice = int(input("Voer hier uw gekozen OS in. ")) #vraag om gekozen OS
        while not(os_choice == 1 or os_choice == 2 or os_choice == 3): #controleer of os_choice wel één van de bovenstaande opties is
            print("Kies alstublieft één van de bovenstaande opties.") #vraag om correcte optie
            os_choice = int(input("Voer hier uw gekozen OS in.")) #vraag opnieuw om gekozen OS
        if os_choice == 1: #maak een string aan voor het gekozen OS, voor de log en andere mogelijke zaken waarbij de volledige naam noodzakelijk is
            os_choice_verbose = str("Windows")
        elif os_choice == 2:
            os_choice_verbose = str("Ubuntu")
        elif os_choice == 3:
            os_choice_verbose = str("Raspbian")
        defaultlogger.logging.info("Het OS " + os_choice_verbose + " is gekozen.")  # maak een log entry aan voor de OS keuze
        return os_choice #passeer os_choice naar main.py als os_selection zodat deze ook in de main gebruikt kan worden
    except ValueError: #vang value error af
        print("Voer alstublieft een getal in.")
        return os_choice_input() #keer terug naar os_choice