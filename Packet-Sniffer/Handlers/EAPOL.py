import Globals.MyGlobals as confg
import random
import string
from scapy.all import *
from rssi import get_rssi
from Classes.classes import *

def handler(packet):
    """
        Handler for eapol packets.
    """
    confg.HANDSHAKES[packet.addr3].append(packet);
    confg.APS[packet.addr3].add_eapol();
    filename = ("/root/pcaps/"+str(confg.APS[packet.addr3].mssid)+"_"+str(packet.addr3)[-5:].replace(":", "")+".pcap");
    if len(confg.HANDSHAKES[packet.addr3]) >= 6:
        if not os.path.isfile(filename):
            os.system("touch "+filename);
        wrpcap(filename, confg.HANDSHAKES[packet.addr3], append=True);
        confg.HANDSHAKES[packet.addr3] = [];
    return;
