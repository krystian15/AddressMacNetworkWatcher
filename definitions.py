import os
SECRET_KEY = os.urandom(32)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_STORAGE_DIR = os.path.join(ROOT_DIR, 'data_storage')

ARP_INTERFACES = ('wlan0', 'eth0')
ARP_INTERFACE = ARP_INTERFACES[0]

NETWORK_TIMER_INTERVAL = 10
