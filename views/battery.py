from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import BatteryForm
from battery import Battery
import json

battery = Blueprint('battery', __name__)


@battery.route("/#battery", methods=["GET", "POST"])
def create_battery():
    form = BatteryForm()
    if request.method == 'POST':
        new_battery = session['battery']
        if form.validate_on_submit():
            new_battery = Battery()
            form.populate_obj(new_battery)
            new_battery.complete_fields()
            new_battery.compute_disposal()
            new_battery.compute_e_manufactoring()
            new_battery_encoded = json.dumps(new_battery.__dict__)
            session['battery'] = new_battery_encoded
            return redirect(url_for('home.index'))
    elif session['battery']:
        battery = json.loads(session['battery'])
        for e, key in zip(form, battery):
            e.data = battery[key]
    return render_template("index.html", form=form, device=None, battery=None,
                           solar_panel=None, maintenance=None)
