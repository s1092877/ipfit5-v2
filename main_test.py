#tijdelijk testbestand om snel en zonder complicaties diverse modules en features te testen
#lever dit script niet op

import defaultlogger
import toolinputs
import os
import ddimage
import hashing_test_sha.py

evidenceid = "3"
ifile = ddimage.imager(evidenceid)
mfile = "images/" + evidenceid + ".raw"

hashtest = hashing_test_sha.hasher(ifile,mfile)

if hashtest is True:
    print("de hashes kloppen")
elif hashtest is False:
    print("de hashes kloppen niet :(")