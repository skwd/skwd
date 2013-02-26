#!/usr/bin/python

from scapy.all import *


def dhcprespond(x):
	x.show()

def main():
	conf.checkIPaddr = False
	fam,hw = get_if_raw_hwaddr(conf.iface)
	ret = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=hw)/DHCP(options=[("message-type","discover"),"end"])
	ans,unans = srp(ret, multi=True)
	for p in ans:
		print p[1][Ether].src, p[1][IP].src
	#sniff(prn=dhcprespond,filter='port 67 or port 68')

if __name__ == '__main__':
	main()
