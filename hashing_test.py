import hashlib
BLOCKSIZE = 65536
hasher = hashlib.md5() #we maken een md5 hash
with open('2018-11-13-raspbian-stretch-full.img', 'rb') as afile: #Hierbij open je het het bestand dat je wil hashen, dat is nu raspian strech
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest()) # hierbij print je de hash uit die je net hebt gemaakt