import subprocess
import defaultlogger
import toolinputs


def imager(evidenceid):

    try:
        ifile = toolinputs.image_input()
        cmd = subprocess.check_output(['dd', 'if=' + ifile, 'of=images/' + "image" + evidenceid, 'bs=' + bsize])
        defaultlogger.logging.info("het pad van de geimagde usb stick is " + ifile + ", locatie en naam van image is" + ofile + "met blocksize van" + bsize)
        return cmd
    except:
        print("Niet gelukt")

