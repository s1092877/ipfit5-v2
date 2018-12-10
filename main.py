import defaultlogger #importeer de default_logger apart; deze klasse handelt al het loggen af
import toolinputs #importeert de inputs-klasse, voor alle mogelijk benodigde variabelen
import main_test #test

print("IPFIT5 tool")
print("Maarten Liang & Danilo di Summa")

evidenceid = toolinputs.evidenceid_input() #roept toolinputs aan om het evidence ID in te voeren.

main_test.test(evidenceid)