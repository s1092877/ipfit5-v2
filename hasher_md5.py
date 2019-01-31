import subprocess # importeer subprocess zodat er linux tools aangeroepen kunnen worden

def hasher(ifile, mfile): # maak een def aan voor het hashen die ifile en mfile meekrijgt voor het usb station en image

    md5_hash_ifile = subprocess.call(['md5sum', ifile]) # genereer met md5sum via subprocess een hash en sla dit op als var
    defaultlogger.logging.info("De hash van de USB-stick is" + md5_hash_ifile)  # log hashes
    md5_hash_mfile = subprocess.call(['md5sum', mfile]) # genereer met md5sum via subprocess een hash en sla dit op als var
    defaultlogger.logging.info("De hash van de USB-stick is" + md5_hash_mfile)  # log de hashes

    if md5_hash_ifile == md5_hash_mfile: # als de hashes overeen komen:
        defaultlogger.logging.info("De hashes komen overeen.")  # log dit
        return True # geef true door aan het aanroepende script
    elif md5_hash_ifile != md5_hash_mfile: # als de hashes niet overeen komen:
        defaultlogger.logging.info("De hashes komen niet overeen.")  # log dit
        return False # geef false door aan het aanroepende script
