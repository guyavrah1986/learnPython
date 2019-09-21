import datetime
from scapy.layers.l2 import Ether


class BasePacketParser:

    def __init__(self, packet_data):
        func_name = "BasePacketParser::__init__ - "
        self.packet_data = packet_data

    def packet_parser_get_packet_time(self):
        func_name = "BasePacketParser::packet_parser_get_packet_time - "
        ether_pkt = Ether(self.packet_data)
        #print(func_name + "packet time is:" + str(ether_pkt.time.__format__()))
        packet_time_utc_format = datetime.datetime.fromtimestamp(int(ether_pkt.time) / 1e3)
        #packet_time_utc_format = datetime.utcfromtimestamp(float(ether_pkt.time))
        return ether_pkt.time
