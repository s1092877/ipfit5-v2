import subprocess
import defaultlogger
import toolinputs


def imager():

    try:
        ifile = toolinputs.image_input()
        cmd = subprocess.check_output(['dd', 'if=' + ifile, 'of=logs/' + ofile, 'bs=' + bsize])
        defaultlogger.logging.info("het pad van de geimagde usb stick is " + ifile + ", locatie en naam van image is" + ofile + "met blocksize van" + bsize)
        return cmd
    except:
        print("Niet gelukt")
