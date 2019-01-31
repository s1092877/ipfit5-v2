import subprocess # importeer subprocess zodat er linux tools aangeroepen kunnen worden
import defaultlogger # importeer de logging module zodat deze aangeroepen kan worden


def imager(evidenceid,ifile): # maak een def aan om een image te maken; geef het evidence id en usb station mee
    print("Er wordt nu een image van de USB-stick gemaakt. Even geduld aub...") # meld dat er een image gemaakt wordt
    cmd = subprocess.call(['dd', 'if=' + ifile, 'of=images/' + "image" + evidenceid + '.raw']) # maak via subprocess een image; gebruik hierbij de linux tool DD
    ofile = 'images/image' + evidenceid + '.raw' # maak van de output een variabele
    defaultlogger.logging.info("Er werd met DD een image gemaakt.") # log dit
    defaultlogger.logging.info("Het pad van de geimagede usb stick is " + ifile + ", locatie en naam van image is" + ("image " + evidenceid)) # log dit weg
    return ofile # geef de output file locatie door aan het aanroepende script

