import json
from definitions import WHITE_LIST_NAME, WHITE_LIST_DIR


def write_json_file(data, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def add_new_user(email: str, address_mac: str):
    email: str
    address_mac: str

    with open(WHITE_LIST_DIR) as user_file:
        white_list_hosts_file = json.load(user_file)
        white_list_hosts = white_list_hosts_file[WHITE_LIST_NAME]

        if email not in white_list_hosts.keys():
            white_list_hosts[email] = []

        if address_mac not in white_list_hosts[email]:
            white_list_hosts[email].append(address_mac)

        write_json_file(white_list_hosts_file, WHITE_LIST_DIR)


# def remove_user_devises(email: str, address_mac: str, remove_one_device: bool = True):
#     email: str
#     address_mac: str
#
#     with open(WHITE_LIST_DIR) as user_file:
#         users = json.load(user_file)
#         ref = users[WHITE_LIST_NAME]
#
#         if email not in ref.keys():
#             ref[email] = []
#
#         if address_mac not in ref[email]:
#             ref[email].append(address_mac)
#
#         write_json_file(users, WHITE_LIST_DIR)


def is_user_exist(address_mac: str) -> bool:
    with open(WHITE_LIST_DIR) as user_file:
        white_list_hosts = json.load(user_file)[WHITE_LIST_NAME]
        if white_list_hosts:
            for email, devices in white_list_hosts.items():
                return any(elem == address_mac for elem in devices)
        return False



