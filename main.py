from flask import Flask, request, render_template, redirect
from getmac import get_mac_address
import os
from mac_addresses.arp import ARPGenerator
from mac_addresses.addresses_helpers import get_ip_address
from forms.mac_form import MacForm
from users.user_subscribe import add_new_user, is_user_exist

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

arp_output = ARPGenerator().arp_output


@app.route('/', methods=['GET', 'POST'])
def home():
    form = MacForm()
    address_mac = get_mac_address(ip=request.remote_addr)

    if form.validate_on_submit():
        fullname = form.fullname.data
        mattermost_nickname = form.mattermost_nickname.data

        add_new_user(fullname, address_mac, mattermost_nickname)
        return redirect('/thank-you')

    showForm = is_user_exist(address_mac)
    return render_template('index.html', showForm=showForm, form=form)


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
