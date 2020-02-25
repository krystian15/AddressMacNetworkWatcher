def get_new_online_users(prev_online_hosts, online_hosts):
    return set(online_hosts) - set(prev_online_hosts)


def get_new_offline_users(online_hosts, prev_online_hosts):
    return set(prev_online_hosts) - set(online_hosts)
