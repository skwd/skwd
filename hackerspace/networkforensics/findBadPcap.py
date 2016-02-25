from scapy.all import *

def GetBadIP(reputationIP):
    f = open(reputationIP,"r")
    BadIP = {}

    for line in f:
        IP,Reason = line.split(" # ")
        BadIP[IP] = Reason
    f.close()
    return BadIP

def CheckIfBadIP(BadIp, pkt):
    if IP in pkt:
        if pkt[IP].dst in BadIp.keys():
            print("[-]Bad IP detected " + pkt[IP].dst + " -> " + BadIp[pkt[IP].dst].split(",")[0])


BadIP = GetBadIP("reputation.generic")
sniff(iface="wlan0", prn=lambda x: CheckIfBadIP(BadIP, x))
