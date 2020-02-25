import threading
from definitions import NETWORK_TIMER_INTERVAL
from mac_addresses.arp import ARPGenerator
from network_watcher.date_helper import is_new_day, get_current_date_timestamp


class NetworkWatcher:

    def __init__(self):
        self.online_hosts = []
        self.offline_hosts = []
        self.today_timestamp = get_current_date_timestamp()

        self.watch_network_hosts()

    def watch_network_hosts(self):
        threading.Timer(NETWORK_TIMER_INTERVAL, self.watch_network_hosts).start()

        print(self.today_timestamp)

        if is_new_day(self.today_timestamp):
            print('New day')

        hosts = ARPGenerator().addresses
        online_hosts = list(map(lambda x: x['mac'], hosts))

        print(online_hosts)

    def new_day_update(self):
        pass

    def is_new_day(self):
        pass


NetworkWatcher()
