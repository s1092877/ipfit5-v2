import subprocess
import defaultlogger
import toolinputs


def imager(evidenceid,ifile):
    cmd = subprocess.call(['dd', 'if=' + ifile, 'of=images/' + "image" + evidenceid + '.raw'])
    print("Er wordt nu een image van de USB-stick gemaakt. Even geduld aub...")
    ofile = 'images/image' + evidenceid + '.raw'
    defaultlogger.logging.info("het pad van de geimagede usb stick is " + ifile + ", locatie en naam van image is" + ("image " + evidenceid))
    return ofile

