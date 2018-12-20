#tijdelijk testbestand om snel en zonder complicaties diverse modules en features te testen
#lever dit script niet op

import defaultlogger
import toolinputs

ostype = toolinputs.detectos()

if ostype == "Linux":
    if os.geteuid() != 0:
        print("Deze tool vereist root-privileges. Zorg ervoor dat deze tool als root gerunt wordt.")
        print("Voer 'exit' in om de tool af te sluiten.")
        exit = input(str(""))
        if exit == "exit" or "Exit":
            sys.exit()

ostype = toolinputs.detectos()
if ostype == "Linux":
    import foremostcarverlinux
    import ddimage
else:
    print("fuck")
