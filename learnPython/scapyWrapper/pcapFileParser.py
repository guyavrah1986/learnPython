from scapy.utils import RawPcapReader


class PcapFileParser:

    def __init__(self, pcap_file_name):
        func_name = "PcapFileParser::__init__ - "
        self.pcap_file_name = pcap_file_name
        print(func_name + "got pcap file name:" + self.pcap_file_name)

    def get_specific_packet(self, packet_number):
        func_name = "PcapFileParser::get_specific_packet - "
        print(func_name + "trying to extract packet number:" + str(packet_number))
        count = 0
        for (pkt_data, pkt_metadata) in RawPcapReader(self.pcap_file_name):
            count += 1
            print(func_name + "extracting packet[" + str(count) + "]")
            if count == packet_number:
                return pkt_data

        print(func_name + "packet number:" + str(packet_number) + " does not exist in this pcap file")
        return None
