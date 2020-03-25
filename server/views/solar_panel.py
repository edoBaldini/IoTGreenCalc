from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import SolarForm
from solar_panel import Solar_Panel
import json
from flask.json import jsonify

solar_panel = Blueprint('solar_panel', __name__)


# @solar_panel.route("/solar_panel", methods=["GET", "POST"])
# def create_solar_panel():
#     form = SolarForm()
#     if request.method == 'POST':
#         solar_panel = session['solar_panel']
#         if form.validate_on_submit():
#             solar_panel = Solar_Panel()
#             form.populate_obj(solar_panel)
#             solar_panel.complete_fields()
#             solar_panel.compute_disposal()
#             solar_panel.compute_e_manufactoring()
#             solar_panel.daily_energy_produced()
#             solar_panel_encoded = json.dumps(solar_panel.__dict__)
#             session['solar_panel'] = solar_panel_encoded
#             return redirect(url_for('home.index'))
#     elif session['solar_panel']:
#         solar_panel = json.loads(session['solar_panel'])
#         for e, key in zip(form, solar_panel):
#             e.data = solar_panel[key]
#     return render_template("index.html", title_form='Solar Panel', form=form)

@solar_panel.route('/solar_panel', methods=["GET", "POST"])
def create_solar_panel():
    response_object = {'status': 'success'}
    if request.method == "POST":
        data = request.get_json()
        print(data)
        solar_panel = Solar_Panel(data)
        solar_panel.complete_fields()
        solar_panel.compute_disposal()
        solar_panel.compute_e_manufactoring()
        solar_panel.daily_energy_produced()
        solar_panel_encoded = json.dumps(solar_panel.__dict__)
        session['solar_panel'] = solar_panel_encoded
        response_object['message'] = 'solar panel added'
    else:
        response_object['solar_panel'] = session['solar_panel']
    return jsonify(response_object)

# example of json request to add a solar panel:
# '{"technology": "mono-Si", "surface": 0.03744, "irradiance": 1.127419355, "s_hours": 9.0, "lifetime": 20.0, "efficiency": 17.0, "kwp": 0, "efficiency_w": 80.0, "weight": 0.54, "disposal": 0.08650800000000002, "e_manufactoring": 205.02518400000002, "e_produced": 0.025832875358534402}'
