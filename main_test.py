#tijdelijk testbestand om snel en zonder complicaties diverse modules en features te testen
#lever dit script niet op

import defaultlogger
import toolinputs
import os
import ddimage
import hashing_test_sha
import foremostcarverlinux
import sys

try:
    ostype = toolinputs.detectos()

    if ostype == "Linux":
        if os.geteuid() != 0:
            print("Deze tool vereist root-privileges. Zorg ervoor dat deze tool als root gerunt wordt.")
            print("Voer 'exit' in om de tool af te sluiten.")
            exit = input(str(""))
            if exit == "exit" or "Exit":
                sys.exit()
        else:
            import foremostcarverlinux
            import ddimage

    if not os.path.exists("logs"):  # controleer of logs directory al bestaat
        os.makedirs("logs")  # maak indien nodig een directory aan voor logs

    if not os.path.exists("images"):  # controleer of logs directory al bestaat
        os.makedirs("images")  # maak indien nodig een directory aan voor logs

    print("IPFIT5 tool")  # naam tool
    print("Maarten Liang & Danilo di Summa")  # naam groepsleden
    print("Deze tool kan op ieder moment afgesloten worden door middel van de toetsencombinatie ctrl + c.")

    evidenceid = toolinputs.evidenceid_input()  # roept toolinputs aan om het evidence ID in te voeren
    ifile = toolinputs.image_input_station()
    image = ddimage.imager(evidenceid,ifile)
    hashing_test_sha.hasher(ifile,image)
    carve = foremostcarverlinux.carve(evidenceid)

except KeyboardInterrupt:
    defaultlogger.logging.info("De tool werd voortijdig afgesloten.")
    print('De tool is afgesloten.')
