from flask import (Blueprint, render_template, request, session, redirect,
                   url_for)
from device import Device
from battery import Battery
from solar_panel import Solar_Panel

home = Blueprint('home', __name__)


@home.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form.get('component', None) == 'device':
            session['device'] = Device().__dict__
            return redirect(url_for("device.create_device"))
        if request.form.get('component', None) == 'battery':
            session['battery'] = Battery().__dict__
            return redirect(url_for("battery.create_battery"))
        if request.form.get('component', None) == 'solar_panel':
            session['solar_panel'] = Solar_Panel().__dict__
            return redirect(url_for("solar_panel.create_solar_panel"))
        if request.form.get('battery', None) == 'delete':
            session['battery'] = None
        if request.form.get('solar_panel', None) == 'delete':
            session['solar_panel'] = None
        if request.form.get('device', None) == 'delete':
            session['device'] = None

    return render_template("index.html", session=session)

