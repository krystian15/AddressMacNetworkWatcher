import threading
from definitions import NETWORK_TIMER_INTERVAL
from mac_addresses.address_mac_generator import AddressMacGenerator
from network_watcher.date_helper import is_new_day, get_current_date_timestamp
from network_watcher.hosts_helper import get_new_offline_users, get_new_online_users


class NetworkWatcher:

    def __init__(self):
        self.online_hosts = []
        self.offline_hosts = []
        self.today_timestamp = get_current_date_timestamp()

        self.watch_network_hosts()

    def watch_network_hosts(self):
        threading.Timer(NETWORK_TIMER_INTERVAL, self.watch_network_hosts).start()

        if is_new_day(self.today_timestamp):
            print('New day')

        online_hosts = AddressMacGenerator().addresses

        print(f'Online {get_new_online_users(self.online_hosts, online_hosts)}')
        print(f'Offline {get_new_offline_users(online_hosts, self.online_hosts)}')

        self.online_hosts = online_hosts

    def new_day_update(self):
        pass

    def new_online_users_update(self):
        pass

    def new_offline_users_update(self):
        pass


NetworkWatcher()
