#deze klasse dient om alle mogelijke inputs af te handelen, en controleert alle variabelen die hierbij aangemaakt worden

import defaultlogger #importeer de default_logger apart; deze klasse handelt al het loggen af

 # maakt evidenceid als global aan zodat deze ook in andere klasses gebruikt kan worden.

def evidenceid_input(): #deze def maakt het evidence id aan en logt dit meteen weg
    evidenceid = input(str("Voer het evidence ID van de USB-stick in. "))
    defaultlogger.loggerconfig(evidenceid)
    defaultlogger.logging.info("Evidence ID " + evidenceid + " is ingevoerd en de tool is gestart.")
    return evidenceid