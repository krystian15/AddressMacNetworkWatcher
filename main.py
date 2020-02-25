from flask import Flask, request, render_template, redirect
from getmac import get_mac_address
import os
from mac_addresses.addresses_helpers import get_ip_address
from forms.mac_form import EmailForm
from users.user_subscribe import add_new_user, is_user_exist

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def home():
    form = EmailForm()
    print(request.remote_addr)
    address_mac = get_mac_address(interface='eth0', ip=request.remote_addr)

    print(address_mac)

    if form.validate_on_submit():
        email = form.email.data

        add_new_user(email, address_mac)
        return redirect('/thank-you')

    hideForm = is_user_exist(address_mac)
    return render_template('index.html', hideForm=hideForm, form=form)


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
