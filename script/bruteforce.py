#!/usr/bin/python

import crypt
from itertools import product

key = product("abcdefghijklmnopqrstuvwxyz1234567890",repeat=6)
b = 0
found = False
try:
        for i in key:
                p = "".join(i)
                c = crypt.crypt(p,"$6$6fYFH5hT$")
                if c == "$6$6fYFH5hT$j9CaB8cpllsv4RWvSv23f2lpvpAgZEgu1jhG4be6TFiz44wZRXKriTYLt0FtSwyboiXnHxgBaXnPMTmIBBixr.":
                        print "password found : " + p
                        found = True
        b = (b + 1) % 100000
        if b== 0:
                print "100000 try: " +  p
except:
        print "it's seen to long. yeah I know!"
