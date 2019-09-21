import abc


class IgpPacketParserInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def packet_parsing_get_packet_protocol_type(self):
        pass