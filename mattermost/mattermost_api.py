import requests
from definitions import BOT_TOKEN, API_URL


class MattermostRESTAPI:

    def __init__(self):
        self.chanel_id = 'd7odg6aizpnoiyh81e74ehz8me'
        self.headers = {
            'content-type': 'application/json',
            'Accept-Charset': 'UTF-8',
            'authorization': f'Bearer {BOT_TOKEN}'
        }

    def send_message(self, message: str):
        payload = {
            "channel_id": self.chanel_id,
            "message": message
        }
        return requests.post(f'{API_URL}/posts', json=payload, headers=self.headers)

    def delete_message(self, message_id):
        return requests.delete(f'{API_URL}/posts/{message_id}', headers=self.headers)

    # def edit_message(self, message_id):
    #     return requests.put(f'{API_URL}/posts/{message_id}',
    #                         json={'id': '3pqnosa19j8oir5dfyeomcz39w', 'message': 'Update'},
    #                         headers=self.headers)

    def clear_channel(self):
        pass


if __name__ == "__main__":
    res = MattermostRESTAPI().send_message('test')
    print(res.text)
