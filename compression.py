import gzip
import shutil
import ddimage
import defaultlogger


def compressie(image):



    with open(image, 'rb') as f_in, gzip.open('compressions/' +image + '.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    defaultlogger.logging.info("de image wordt gecomprimeerd" )


