import gzip # importeer gzip; met deze library kunnen dingen gecomprimeerd worden in .tar.gz
import shutil
import defaultlogger # importeer de logging module zodat deze aangeroepen kan worden voor het loggen

def compressie(image):
    print("Het comprimeren van de image wordt nu gestart. Even geduld aub...") # meld dat de image gecomprimeerd wordt
    with open(image, 'rb') as f_in, gzip.open('compressions/' +image + '.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    defaultlogger.logging.info("De image werd gecomprimeerd.") # log dit


