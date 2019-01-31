# de main handelt effectief alles in de tool af en stuurt de modules aan; zonder me main functioneren de andere modules niet

import defaultlogger # importeer de logging module zodat deze aangeroepen kan worden
import toolinputs  # importeer toolinputs zodat inputs afgehandeld kunnen worden
import os # importeer os zodat er dingen gedaan kunnen worden met het systeem wat gedraait wordt
import ddimage # importeer ddimage zodat er geimaged kan worden vanuit de main
import hasher_md5 # importeer de hasher zodat er hashes gegeneerd kunnen worden
import foremostcarverlinux # importeer de carver module zodat er gecarved kan worden
import sys # importeer sys; dit wordt gebruikt voor sys.exit om de tool af te sluiten
import compression # importeer de compression module zodat gemaakte images gecomprimeerd kunnen worden

try: # zet de gehele main in een try loop zodat KeyboardInterrupt afgevangen kan worden
    ostype = toolinputs.detectos()

    if ostype == "Linux": # als het OS type Linux is:
        if os.geteuid() != 0: # als het uid niet 0 is, oftewel niet root:
            print("Deze tool vereist root-privileges. Zorg ervoor dat deze tool als root gerunt wordt.") # meld dit
            print("Druk op enter om de tool af te sluiten.") # geef de optie om de tool af te sluiten
            exit = input(str(""))
            if exit == "": # sluit als er op enter gedrukt wordt de tool af met sys.exit
                defaultlogger.logging.info("De tool werd voortijdig afgesloten door gebrek aan rechten.")  # log dit
                sys.exit()
        else: # als de tool als root gedraait wordt:
            import foremostcarverlinux # importeer de carver en imager, die linux tools gebruiken
            import ddimage
    elif ostype == "Windows": # als het OS type Windows is
        print("Windows wordt helaas niet ondersteund.") # meld dit
        print("De tool wordt nu afgesloten.")
        sleep(3.0) # wacht 3 seconden zodat de meldingen gelezen kunnen worden
        sys.exit() # sluit de tool af

    if not os.path.exists("logs"):  # controleer of logs directory al bestaat
        os.makedirs("logs")  # maak indien nodig een directory aan voor logs
        defaultlogger.logging.info("Er werd een logging directory aangemaakt.")  # log dit

    if not os.path.exists("images"):  # controleer of images directory al bestaat
        os.makedirs("images")  # maak indien nodig een directory aan voor images
        defaultlogger.logging.info("Er werd een image directory aangemaakt.")  # log dit

    if not os.path.exists("compressions/images"): # controleer of the images map al bestaat
        os.makedirs("compressions/images") # maak indien nodig een directory aan voor images
        defaultlogger.logging.info("Er werd een compressie directory aangemaakt.")  # log dit

    print("IPFIT5 tool")  # naam tool
    print("Maarten Liang & Danilo di Summa")  # naam groepsleden
    print("Deze tool kan op ieder moment afgesloten worden door middel van de toetsencombinatie ctrl + c.") # instructies

    while True: # zet de tool in een infinite loop zodat deze constant opnieuw uitgevoerd kan worden indien nodig
        defaultlogger.logging.info("De tool werd gestart.")  # log dit
        evidenceid = toolinputs.evidenceid_input()  # roept toolinputs aan om het evidence ID in te voeren
        ifile = toolinputs.image_input_station() # maak ifile aan als resultaat van de station input zodat deze doorgegeven kan worden
        image = ddimage.imager(evidenceid,ifile) # roep de imager aan en maak een variabele van de output
        hash = hasher_md5.hasher(ifile, image) # roep de hasher aan en geef ifile en image mee hieraan
        if hash == False: # als de hasher False teruggeeft:
            print('De hashes voor de USB en image komen niet overeen!') # meld dit
            print('Druk op enter als u het imaging-proces opnieuw wil uitvoeren. Voer iets anders in als u door wil gaan.')
            if input("") == "": # geef de optie om het imagen opnieuw uit te voeren
                image = ddimage.imager(evidenceid,ifile) # roep indien nodig de imager opnieuw aan
        carve = foremostcarverlinux.carve(evidenceid,image) # roep de carver aan om de gemaakte image te carven
        compression.compressie(image) # roep de compressor aan om de gemaakte image te comprimeren
        print("De tool is nu klaar met draaien.") # meld dat de tool klaar is
        repeat = input("Druk op enter om de tool nogmaals uit te voeren. Druk op ctrl + c of voer iets anders in om de tool af te sluiten.")
        if repeat == "": # als er op enter gedrukt, voer de tool nogmaals uit
            defaultlogger.logging.info("De tool werd nogmaals uitgevoerd.") # log dit
        if repeat != "": # als er iets anders ingevoerd wordt:
            defaultlogger.logging.info("De tool werd afgesloten.") # log dit
            break # breek uit de infinite loop


except KeyboardInterrupt: # vang keyboardinterrupt, ofwel ctrl + c, netjes af
    defaultlogger.logging.info("De tool werd voortijdig afgesloten.") # log dit
    print('De tool is afgesloten.') # meld dat de tool is afgesloten.
