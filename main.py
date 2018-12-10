import defaultlogger #importeer de default_logger apart; deze klasse handelt al het loggen af
import toolinputs #importeert de inputs-klasse, voor alle mogelijk benodigde variabelen
import os #importeert de os-library om directories aan te maken

if not os.path.exists("logs"): #controleer of logs directory al bestaat
    os.makedirs("logs") #maak indien nodig een directory aan voor logs

print("IPFIT5 tool") #naam tool
print("Maarten Liang & Danilo di Summa") #naam groepsleden

evidenceid = toolinputs.evidenceid_input() #roept toolinputs aan om het evidence ID in te voeren.

os_selection = toolinputs.os_choice_input() #roept toolinputs aan om een OS te selecteren