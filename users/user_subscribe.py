import json
from definitions import DATA_STORAGE_DIR

users_file_path = f'{DATA_STORAGE_DIR}/users.json'


def add_new_user(fullname, address_mac):

    with open(users_file_path) as json_file:
        data = json.load(json_file)
        temp = data['users']

        temp.append({
            "name": fullname,
            "mac": address_mac
        })
