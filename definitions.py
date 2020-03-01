import os
from typing import Tuple, Union
from mac_addresses.addresses_helpers import get_ip_address

HOST = get_ip_address()
PORT = 8000

SECRET_KEY: bytes = os.urandom(32)
ROOT_DIR: Union[bytes, str] = os.path.dirname(os.path.abspath(__file__))
DATA_STORAGE_DIR: Union[bytes, str] = os.path.join(ROOT_DIR, 'data_storage')

WHITE_LIST_NAME = 'white_list'
BLACK_LIST_NAME = 'black_list'

WHITE_LIST_DIR = f'{DATA_STORAGE_DIR}/{WHITE_LIST_NAME}.json'
BLACK_LIST_DIR = f'{DATA_STORAGE_DIR}/{BLACK_LIST_NAME}.json'

ARP_INTERFACES: Tuple[str, str, str, str] = ('wlan0', 'eth0', 'en1', 'enp0s3')
ARP_INTERFACE: str = ARP_INTERFACES[0]


NETWORK_TIMER_INTERVAL: int = 100

API_URL: str = 'https://mattermost.ageno.work/api/v4'
BOT_TOKEN: str = 'x9quyx7ezpnc7mxobhphkm9n3y'


