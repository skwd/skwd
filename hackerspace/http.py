#!/usr/bin/python

from scapy.all import *

pkts = rdpcap("HTTP.pcap")

get = pkts.filter(lambda x: x if Raw in x and "GET" in x[Raw].load else False)


for pkt in get:
    src = pkt[IP].src
    dst = pkt[IP].dst
    url, host = pkt[Raw].load.split("\r\n")[0:2]
    print src + "\t--->  " + host.split(": ")[1] + url.split(" ")[1]
