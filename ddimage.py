import subprocess
import defaultlogger
import toolinputs


def imager(evidenceid):
    ifile = toolinputs.image_input_station()
    #bsize = toolinputs.image_input_blocksize()
    cmd = subprocess.call(['dd', 'if=' + ifile, 'of=images/' + "image" + evidenceid + '.raw'])
    progress = cmd.stdout.readline()
    print(progress)
    defaultlogger.logging.info("het pad van de geimagede usb stick is " + ifile + ", locatie en naam van image is" + ("image" + evidenceid) + "met blocksize van" + bsize)
    return ifile


