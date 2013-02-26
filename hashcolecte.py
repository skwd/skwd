#!/usr/bin/python
import re

f = open("/etc/shadow","r")

for i in f:
	try:
		print re.search(r'[A-Za-z0-9]+\:\$6\$[A-Za-z0-9]{8}\$[A-Za-z0-9/.]{86}',i).group()
	except:
		pass
