#!/usr/bin/python

import crypt 

f = open("dic",'r')

for i in f.readlines():
	c = crypt.crypt(i.strip('\n'),"$6$6fYFH5hT$")
	if c == "$6$6fYFH5hT$j9CaB8cpllsv4RWvSv23f2lpvpAgZEgu1jhG4be6TFiz44wZRXKriTYLt0FtSwyboiXnHxgBaXnPMTmIBBixr.":
		print "password found : " + i.strip('\n')
		
print "end" 
