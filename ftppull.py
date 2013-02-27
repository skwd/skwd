#!/usr/bin/python

from ftplib import FTP
from sys import argv
import nmap

def scanftp():
	nm = nmap.PortScanner()
	nm.scan(argv[1],"21")
	ip = []
	for i in nm.all_hosts():
		if nm[i]['tcp'][21]['state'] == 'open':
			ip.append(i)
	return ip
def connectftp(ip):
	anncon =[]
	for i in ip:
		try:
			ftp = FTP(i)
			ftp.login()
			anncon.append(i)
		except:
			pass
	return anncon

def main():
	ip = scanftp()
	anocon = connectftp(ip)
	for i in anocon:
		print i	
if __name__=="__main__":
	main()

