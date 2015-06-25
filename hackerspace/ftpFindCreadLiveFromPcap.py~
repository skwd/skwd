#!/usr/bin/python

from scapy.all import *
import re


def readftpcap(x):
	raw = x.sprintf("%Raw.load%")
	src = x.sprintf("%IP.src%")
	dst = x.sprintf("%IP.dst%")
	sport=x.sprintf("%IP.sport%")
	if raw != "??":
		try:	
			if sport == "21":
				print "[*] " + dst + " <----- " + src
			else:
				print "[*] " + src + " -----> " + dst
			print re.search(r'(USER|PASS|[0-9]{3}) (.*)',raw).groups()
		except:
			pass	

p=rdpcap("FTP.pcap")
for pkt in p:
	readftpcap(pkt)

