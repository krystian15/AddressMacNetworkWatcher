import subprocess
import re
from typing import Dict, List

from mac_addresses.helpers import is_address_mac, add_missing_zero_to_address_mac


class ARPGenerator:
    os_arp_output: str
    arp_pattern: str
    addresses: List

    def __init__(self):
        self.os_arp_output = ""
        self.addresses = []
        self.arp_pattern = r"\((.*?)\) :?.*? (.*?) "

        self.set_system_addresses_mac()
        self.convert_arp_output_to_addresses_object()

    def set_system_addresses_mac(self):
        self.os_arp_output = subprocess.check_output("arp -a", shell=True).decode('UTF-8')

    def convert_arp_output_to_addresses_object(self):

        arp_output: str = self.os_arp_output
        arp_pattern: str = self.arp_pattern

        results = re.finditer(arp_pattern, arp_output, re.MULTILINE)
        converted_addresses: List[Dict[str, str]] = []

        for matchNum, match in enumerate(results, start=1):

            new_record_addresses: Dict[str, str] = {
                'ip': '',
                'mac': ''
            }

            groupNum: int
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                address: str = match.group(groupNum)

                if is_address_mac(address):
                    new_record_addresses['mac'] = add_missing_zero_to_address_mac(address)
                    continue

                new_record_addresses['ip'] = address
            converted_addresses.append(new_record_addresses)

        self.addresses = converted_addresses


if __name__ == '__main__':
    arp = ARPGenerator()
    print(arp.addresses)

