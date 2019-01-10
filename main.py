import defaultlogger #importeer de default_logger apart; deze klasse handelt al het loggen af
import toolinputs #importeert de inputs-klasse, voor alle mogelijk benodigde variabelen
import os #importeert de os-library om directories aan te maken
import sys

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

if not os.path.exists("logs"): #controleer of logs directory al bestaat
    os.makedirs("logs") #maak indien nodig een directory aan voor logs

if not os.path.exists("images"): #controleer of logs directory al bestaat
    os.makedirs("images") #maak indien nodig een directory aan voor logs



print("IPFIT5 tool") #naam tool
print("Maarten Liang & Danilo di Summa") #naam groepsleden
print("Deze tool kan op ieder moment afgesloten worden door 'exit' in te voeren.")

evidenceid = toolinputs.evidenceid_input() #roept toolinputs aan om het evidence ID in te voeren.