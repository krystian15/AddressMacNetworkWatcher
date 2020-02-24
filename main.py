from flask import Flask, request, render_template, redirect, flash
from getmac import get_mac_address
import json
import os
from mac_addresses.arp import ARPGenerator
from mac_addresses.addresses_helpers import get_ip_address
from forms.mac_form import MacForm
from users.user_subscribe import add_new_user

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

arp_output = ARPGenerator().arp_output

# with open('data_storage/users.json.sample') as f:
#     users: object = json.load(f)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = MacForm()
    if form.validate_on_submit():

        fullname = form.fullname.data
        address_mac = get_mac_address(ip=request.remote_addr)

        add_new_user(fullname, address_mac)

        return redirect('/thank-you')
    return render_template('index.html', form=form)

    #
    # return users.get(address_mac, 'Not found')


@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')


@app.before_request
def before_request_func():
    print(request.remote_addr)


host = get_ip_address()
port = 8000

if __name__ == '__main__':
    app.run(host=host, port=port)
