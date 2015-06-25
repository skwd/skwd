#!/usr/bin/python

from scapy.all import *

def Reply(pkt):
    if pkt[ICMP].type == 8 and pkt[ICMP].load == "forger c full faf":
        src = pkt.sprintf("%IP.src%")
        print "[+]reply to " + src
        response = IP(dst=src)/ICMP(code=0, type=0)/Raw(load="Good Job")
        send(response)

sniff(iface="eth0", filter="icmp",prn=Reply)


#ping = IP(dst="192.168.69.40")/ICMP()/Raw(load="forger c full faf")
#sr(ping) 
