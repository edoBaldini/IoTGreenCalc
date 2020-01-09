from flask import (Blueprint, render_template, request, session, redirect,
                   url_for)
from device import Device

home = Blueprint('home', __name__)


@home.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form.get('component', None) == 'device':
            session['device'] = Device().__dict__
            return redirect(url_for("device.create_device"))
    return render_template("index.html", session=session)




