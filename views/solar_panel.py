from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import SolarForm
from solar_panel import Solar_Panel
import json

solar_panel = Blueprint('solar_panel', __name__)


@solar_panel.route("/solar_panel", methods=["GET", "POST"])
def create_solar_panel():
    form = SolarForm()
    if request.method == 'POST':
        solar_panel = session['solar_panel']
        if form.validate_on_submit():
            solar_panel = Solar_Panel()
            form.populate_obj(solar_panel)
            solar_panel.complete_fields()
            solar_panel.compute_disposal()
            solar_panel.compute_e_manufactoring()
            solar_panel.daily_energy_produced()
            solar_panel_encoded = json.dumps(solar_panel.__dict__)
            session['solar_panel'] = solar_panel_encoded
            return redirect(url_for('home.index'))
    elif session['solar_panel']:
        solar_panel = json.loads(session['solar_panel'])
        for e, key in zip(form, solar_panel):
            e.data = solar_panel[key]
    return render_template("index.html", title_form='Solar Panel', form=form)
