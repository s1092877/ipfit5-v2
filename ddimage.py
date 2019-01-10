import subprocess
import defaultlogger
import toolinputs


def imager(evidenceid,ifile):
    #bsize = toolinputs.image_input_blocksize()
    cmd = subprocess.call(['dd', 'if=' + ifile, 'of=images/' + "image" + evidenceid + '.raw'])
    ofile = '/images/image' + evidenceid + '.raw'
    defaultlogger.logging.info("het pad van de geimagede usb stick is " + ifile + ", locatie en naam van image is" + ("image" + evidenceid))
    return ofile


