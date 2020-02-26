from flask import Flask, request, render_template, redirect
from getmac import get_mac_address
from mac_addresses.addresses_helpers import get_ip_address
from forms.mac_form import EmailForm
from users.user_subscribe import add_new_user, is_user_exist
from definitions import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def home():
    form = EmailForm()
    address_mac = get_mac_address(interface='eth0', ip=request.remote_addr)

    if form.validate_on_submit():
        email = form.email.data

        add_new_user(email, address_mac)
        return redirect('/thank-you')

    hide_form = is_user_exist(address_mac)
    return render_template('index.html', hide_form=hide_form, form=form)


@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')


host = get_ip_address()
port = 8000

if __name__ == '__main__':
    app.run(host=host, port=port)
