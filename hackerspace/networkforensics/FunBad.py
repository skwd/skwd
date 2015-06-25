#version scientifique fail ! 
import pandas as pd

Data = pd.DataFrame()


f = open("reputation.generic","r")

for line in f:
    IP,Reason = line.split(" # ")
    Data = Data.append(pd.DataFrame([[IP,Reason]], columns=["IP","Reason"]))
    
f.close()

#version scientifique qui marche  
import pandas as pd

f = open("reputation.generic","r")
IPs = []
Reasons = []

for line in f:
    IP,Reason = line.split(" # ")
    IPs.append(IP)
    Reasons.append(Reason)
d = {"IP" : IPs, "Reason" : Reasons}
Data = pd.DataFrame(data=d)
    
f.close()

# version snifff 
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
            print("[-]Bad IP detected " + pkt[IP].dst + " -> " + BadIp[pkt[IP].dst])


BadIP = GetBadIP("reputation.generic")
sniff(iface="wlan0", prn=lambda x: CheckIfBadIP(BadIP, x))

# version pcap 
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
            print("[-]Bad IP detected " + pkt[IP].dst + " -> " + BadIp[pkt[IP].dst])


BadIP = GetBadIP("./reputation.generic")
pkts =rdpcap("DNS.pcap")

for pkt in pkts:
    CheckIfBadIP(BadIP,pkt)





