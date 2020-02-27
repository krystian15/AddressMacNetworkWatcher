import json
from definitions import WHITE_LIST_DIR, WHITE_LIST_NAME


def filter_white_list_hosts(hosts: list) -> set:
    users = []

    with open(WHITE_LIST_DIR) as white_list_hosts_file:
        white_list_hosts = json.load(white_list_hosts_file)[WHITE_LIST_NAME]

        if white_list_hosts:
            for email, devices in white_list_hosts.items():
                if any(elem in hosts for elem in devices):
                    users.append(email)
        return set(users)


def get_new_online_users(prev_online_hosts, online_hosts):
    return filter_white_list_hosts(list(set(online_hosts) - set(prev_online_hosts)))


def get_new_offline_users(online_hosts, prev_online_hosts):
    return filter_white_list_hosts(list(set(prev_online_hosts) - set(online_hosts)))
