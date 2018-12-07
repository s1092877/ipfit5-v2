#tijdelijk testbestand om snel en zonder complicaties diverse modules en features te testen
#lever dit script niet op

import default_logger

global evidenceid
evidenceid = str(input("test"))

default_logger.loggerconfig(evidenceid)
default_logger.logging.info("schurft")
