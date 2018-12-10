import defaultlogger #importeer de default_logger apart; deze klasse handelt al het loggen af
import toolinputs #importeert de inputs-klasse, voor alle mogelijk benodigde variabelen

print("IPFIT5 tool")
print("Maarten Liang & Danilo di Summa")

toolinputs.evidenceid_input() #roept toolinputs aan om het evidence ID in te voeren.
print(evidenceid)