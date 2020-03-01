from flask import Flask, request, render_template, redirect
from getmac import get_mac_address
from forms.user_device_register_form import UserDeviceRegisterForm
from forms.user_device_unregister_form import UserDeviceUnregisterForm
from users.user_subscribe import add_new_user, is_user_exist, remove_user_devise
from definitions import HOST, PORT, SECRET_KEY, ARP_INTERFACE

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = UserDeviceRegisterForm()
    address_mac = get_mac_address(interface=ARP_INTERFACE, ip=request.remote_addr)

    if form.validate_on_submit():
        email = form.email.data
        add_new_user(email, address_mac)
        return redirect('/thank-you')

    show_form = not is_user_exist(address_mac)
    return render_template('index.html', show_form=show_form, form=form)


@app.route('/thank-you')
def thank_you_page():
    return render_template('thank-you.html')


@app.route('/remove-device', methods=['GET', 'POST'])
def remove_device_page():
    form = UserDeviceUnregisterForm()
    address_mac = get_mac_address(interface=ARP_INTERFACE, ip=request.remote_addr)
    result: str = ''

    if not is_user_exist(address_mac):
        return redirect('/')

    if form.validate_on_submit():
        email = form.email.data
        result = remove_user_devise(email, address_mac)
        if isinstance(result, bool):
            return redirect('/bye-bye')

    return render_template('remove-device.html', form=form, error=result)


@app.route('/bye-bye')
def bye_bye_page():
    return render_template('bye-bye.html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
