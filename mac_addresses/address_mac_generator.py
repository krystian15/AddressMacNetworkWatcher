import re
from typing import List

from mac_addresses.addresses_helpers import add_missing_zero_to_address_mac
from mac_addresses.os_helpers import get_parsed_os_cmd_output
from definitions import ARP_INTERFACE


class AddressMacGenerator:
    arp_output: str
    arp_pattern: str
    addresses: List

    def __init__(self):
        self.arp_output = ''
        self.addresses = []
        self.arp_pattern = r'(?:[0-9a-fA-F]:?){12}'

        self.set_system_addresses_mac()
        self.convert_arp_output_to_addresses_object()

    def set_system_addresses_mac(self):
        self.arp_output = get_parsed_os_cmd_output(f'arp-scan -l --interface={ARP_INTERFACE}')

    def convert_arp_output_to_addresses_object(self):
        self.addresses = list(map(add_missing_zero_to_address_mac, re.findall(self.arp_pattern, self.arp_output)))


if __name__ == '__main__':
    arp = AddressMacGenerator()
    print(arp.addresses)
