import os
from typing import Tuple, Union

SECRET_KEY: bytes = os.urandom(32)
ROOT_DIR: Union[bytes, str] = os.path.dirname(os.path.abspath(__file__))
DATA_STORAGE_DIR: Union[bytes, str] = os.path.join(ROOT_DIR, 'data_storage')

ARP_INTERFACES: Tuple[str, str, str] = ('wlan0', 'eth0', 'en1')
ARP_INTERFACE: str = ARP_INTERFACES[2]


NETWORK_TIMER_INTERVAL: int = 20

API_URL: str = 'https://mattermost.ageno.work/api/v4'
BOT_TOKEN: str = 'x9quyx7ezpnc7mxobhphkm9n3y'


