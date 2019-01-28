import toolinputs
import subprocess

def hasher(ifile, mfile):

    md5_hash_ifile = subprocess.call(['md5sum', ifile])
    md5_hash_mfile = subprocess.call(['md5sum', mfile])

    if md5_hash_ifile == md5_hash_mfile:
        return True
    elif md5_hash_ifile != md5_hash_mfile:
        return False
