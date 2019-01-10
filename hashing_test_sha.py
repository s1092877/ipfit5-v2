import toolinputs
import subprocess

def hasher(ifile, mfile):

    sha256_hash_ifile = subprocess.call(['sha256sum', ifile])
    sha256_hash_mfile = subprocess.call(['sha256sum', mfile])

    if sha256_hash_ifile == sha256_hash_mfile:
        return True
    elif sha256_hash_ifile != sha256_hash_mfile:
        return False
