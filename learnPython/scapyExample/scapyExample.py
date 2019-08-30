#########################################################################################
#########################################################################################
# 0) This is a quick and basic how-to regarding the usage in scapy library.
#
# 1) Installation (Python 3, Ubuntu 18.04):
# ----------------------------------------
# a) pip3 install scapy
# b) toverify it is installed correctly:
# python3 -c "import scapy"
# echo $? (output should be "0")
#########################################################################################
#########################################################################################
from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP

import scapy.contrib.isis

def scapy_usage_example(argv):
    func_name = "scapy_usage_example - "
    print(func_name + "start")
    pcap_file_name = argv[0]
    print(func_name + "got pcap file name:" + pcap_file_name)
    process_pcap(pcap_file_name)
    return 0


def process_pcap(pcap_file_name):
    func_name = "process_pcap - "
    print(func_name + "opening file:" + pcap_file_name)
    count = 0
    interesting_packet_count = 0

    for (pkt_data, pkt_metadata,) in RawPcapReader(pcap_file_name):
        count += 1

        ether_pkt = Ether(pkt_data)
        if 'type' not in ether_pkt.fields:
            # LLC frames will have 'len' instead of 'type'.
            # We disregard those
            continue

        if ether_pkt.type != 0x0800:
            # disregard non-IPv4 packets
            continue

        ip_pkt = ether_pkt[IP]
        if ip_pkt.proto != 6:
            # Ignore non-TCP packet
            continue

        interesting_packet_count += 1

    print(func_name + '{} contains {} packets ({} interesting)'.
          format(pcap_file_name, count, interesting_packet_count))
