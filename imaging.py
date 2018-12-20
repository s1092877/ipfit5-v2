import subprocess
import defaultlogger


def imager():

    try:
        ifile= input("Vul de locatie van de usb in die je wilt imagen ")

        ofile = input("vul de locatie waar je de image wil hebben in met de naam ")

        bsize= input("geef de blocksize op: ")

    except ValueError:
            print("niet correct")

    cmd = subprocess.check_output(['dd','if=' + ifile, 'of=logs/' + ofile, 'bs=' + bsize ])
    defaultlogger.logging.info("het pad van de geimagde usb stick is "+ ifile + ", locatie en naam van image is" + ofile+ "met blocksize van" + bsize)

    return cmd


imager()