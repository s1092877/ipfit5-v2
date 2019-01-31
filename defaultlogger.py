import logging #importeert logging, een library die benodigd is om een logger object aan te maken en deze te configureren

def loggerconfig(evidenceid): ##maakt een def aan om de logger te initialiseren
    logging.basicConfig(filename="logs/" + evidenceid + ".csv", filemode="a", format="%(levelname)s;%(asctime)s;%(message)s", level="INFO")
    #bovenstaande regel is zeer lang; deze regel geeft aan waar de logging output opgeslagen dient te worden
    #filename is het evidence ID zoals opgegeven aan het begin van de primaire functie, opgeslagen als CSV
    #filemode is a voor append; dit betekent dat iedere keer dat basicConfig voor een bestand aangeroepen wordt, deze niet leeg gemaakt wordt
    #dit maakt in feite weinig verschil
    #format slaat de levelname (gebruikelijk INFO), tijdstip en bericht op; semicolons als separators maken dat
    #dit elegant in een spreadsheet geopend kan worden
    logging.debug("init logger") #maakt een logging entry aan voor het aanmaken van de logger als debug