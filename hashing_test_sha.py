import hashlib
import toolinputs

def hasher(ifile, mfile):
    filename1 = ifile
    filename2 = mfile
    sha256_hash_ifile = hashlib.sha256()
    sha256_hash_mfile = hashlib.sha256()
    with open(filename1,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash_ifile.update(byte_block)
            print(sha256_hash_ifile.hexdigest())
    with open(filename2,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash_mfile.update(byte_block)
            print(sha256_hash_mfile.hexdigest())

    if sha256_hash_ifile == sha256_hash_mfile:
        return True
    elif sha256_hash_ifile != sha256_hash_mfile:
        return False