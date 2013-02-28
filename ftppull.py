#!/usr/bin/python

from ftplib import FTP
from sys import argv
import nmap

def scanftp(host,port):
	nm = nmap.PortScanner()
	nm.scan(host,port)
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
			print ftp.getwelcome() + " <------- " + i
		except:
			pass
	return anncon

def main():
	ip = scanftp(argv[1],"21")
	anocon = connectftp(ip)

if __name__=="__main__":
	main()

