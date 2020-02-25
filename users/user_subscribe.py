import json
from definitions import DATA_STORAGE_DIR

users_file_path = f'{DATA_STORAGE_DIR}/users.json'
users_object_name = 'users'


def write_json_file(data, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def add_new_user(fullname: str, address_mac: str, mattermost_nickname: str):
    with open(users_file_path) as user_file:
        users = json.load(user_file)

        users[users_object_name][address_mac] = {
            'name': fullname,
            'mattermost_nickname': mattermost_nickname
        }

        write_json_file(users, users_file_path)


def is_user_exist(address_mac: str) -> bool:
    with open(users_file_path) as user_file:
        users = json.load(user_file)[users_object_name]

        return not bool(users.get(address_mac))
