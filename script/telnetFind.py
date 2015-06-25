#!/usr/bin/python
from sys import argv
import nmap
import telnetlib

def scanftp(host,port):
	nm = nmap.PortScanner()
	nm.scan(host,port)
	ip = []
	for i in nm.all_hosts():
		if nm[i]['tcp'][23]['state'] == 'open':
			ip.append(i)
	return ip
def connectTelnet(ip):
	for i in ip:
		print i 
def main():
	ip = scanftp(argv[1],"23")
	anocon = connectTelnet(ip)

if __name__=="__main__":
	main()

