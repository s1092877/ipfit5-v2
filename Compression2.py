import gzip
import shutil
import ddimage


def compressie(ofile):
    with open(ofile, 'rb') as f_in, gzip.open('/compressions/' + ofile + '.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)