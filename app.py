from flask import Flask, request
from getmac import get_mac_address
import socket
import json
from mac_addresses.arp import ARPGenerator

app = Flask(__name__)

arp_output = ARPGenerator().os_arp_output

with open('users.json') as f:
    users: object = json.load(f)


def get_ip_address():
    host_name = socket.gethostname()
    return socket.gethostbyname(host_name)


@app.route('/')
def hello():
    address_mac = get_mac_address(ip=request.remote_addr)
    return users.get(address_mac, 'Not found')


@app.before_request
def before_request_func():
    print(request.remote_addr)


host = get_ip_address()
port = 8000

if __name__ == '__main__':
    app.run(host=host, port=port)
