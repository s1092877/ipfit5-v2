import subprocess
import toolinputs
import defaultlogger

def carve(evidenceid):
    try:
        cfile = toolinputs.carve_input()
        crv = subprocess.call(["foremost","-t all",cfile,"-o","output" + evidenceid])
        return crv
    except():
        print("Carven mislukt")