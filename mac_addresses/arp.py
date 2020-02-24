import re
from typing import Dict, List

from mac_addresses.addresses_helpers import is_address_mac, add_missing_zero_to_address_mac
from mac_addresses.os_helpers import get_parsed_os_cmd_output


class ARPGenerator:
    arp_output: str
    arp_pattern: str
    addresses: List

    def __init__(self):
        self.arp_output = ""
        self.addresses = []
        self.arp_pattern = r"\((.*?)\) :?.*? (.*?) "

        self.set_system_addresses_mac()
        self.convert_arp_output_to_addresses_object()

    def set_system_addresses_mac(self):
        self.arp_output = get_parsed_os_cmd_output('arp -a')

    def convert_arp_output_to_addresses_object(self):

        results = re.finditer(self.arp_pattern, self.arp_output, re.MULTILINE)
        converted_addresses: List[Dict[str, str]] = []

        for matchNum, match in enumerate(results, start=1):

            new_record_addresses: Dict[str, str] = {
                'ip': '',
                'mac': ''
            }

            group_number: int
            for group_number in range(0, len(match.groups())):
                group_number = group_number + 1
                address: str = match.group(group_number)

                if is_address_mac(address):
                    new_record_addresses['mac'] = add_missing_zero_to_address_mac(address)
                    continue

                new_record_addresses['ip'] = address
            converted_addresses.append(new_record_addresses)

        self.addresses = converted_addresses


if __name__ == '__main__':
    arp = ARPGenerator()
    print(arp.addresses)

