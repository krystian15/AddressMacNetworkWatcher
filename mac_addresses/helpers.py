import socket


def is_address_ip(address: str) -> bool:
    try:
        return bool(socket.inet_aton(address))
    except socket.error:
        return False


def is_address_mac(address: str) -> bool:
    return not is_address_ip(address)


def add_missing_zero_to_address_mac(address: str) -> str:
    address_mac_parts = address.split(':')
    missed_zero_indexes = [i for i, x in enumerate(address_mac_parts) if len(x) < 2]

    if missed_zero_indexes:
        for index in missed_zero_indexes:
            actual_value = address_mac_parts[index]
            address_mac_parts[index] = f'0{actual_value}'

    return ':'.join(address_mac_parts)
