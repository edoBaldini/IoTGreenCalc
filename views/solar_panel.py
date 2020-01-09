from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import SolarForm
from solar_panel import Solar_Panel
import json

solar_panel = Blueprint('solar_panel', __name__)

@solar_panel.route("/solar_panel", methods=["GET", "POST"])
def create_solar_panel():
    return render_template("solar_panel.html", device=session['solar_panel'])

