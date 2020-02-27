import threading
from definitions import NETWORK_TIMER_INTERVAL
from mac_addresses.address_mac_generator import AddressMacGenerator
from network_watcher.date_helper import is_new_day, get_current_date_timestamp
from network_watcher.hosts_helper import get_new_offline_users, get_new_online_users
from mattermost.mattermost_api import MattermostRESTAPI


class NetworkWatcher:

    def __init__(self):
        self.api = MattermostRESTAPI()
        self.online_hosts = AddressMacGenerator().addresses
        self.offline_hosts = []
        self.today_timestamp = get_current_date_timestamp()

        self.watch_network_hosts()

    def watch_network_hosts(self):
        threading.Timer(NETWORK_TIMER_INTERVAL, self.watch_network_hosts).start()

        if is_new_day(self.today_timestamp):
            print('New day')

        online_hosts = AddressMacGenerator().addresses
        new_online_hosts = get_new_online_users(self.online_hosts, online_hosts)
        new_offline_users = get_new_offline_users(online_hosts, self.online_hosts)

        if new_online_hosts:
            self.new_online_users_update(new_online_hosts)

        if new_offline_users:
            self.new_offline_users_update(new_offline_users)

        self.online_hosts = online_hosts

    def new_day_update(self):
        pass

    def new_online_users_update(self, hosts):
        for host in hosts:
            self.api.send_message(message=f"New online user {host}")

    def new_offline_users_update(self, hosts):
        for host in hosts:
            self.api.send_message(message=f"New offline user {host}")


NetworkWatcher()
