#tijdelijk testbestand om snel en zonder complicaties diverse modules en features te testen
#lever dit script niet op

import defaultlogger

global evidenceid
evidenceid = str(input("test"))

defaultlogger.loggerconfig(evidenceid)
defaultlogger.logging.info("schurft")
