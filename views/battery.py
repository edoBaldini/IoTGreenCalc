from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import BatteryForm
from battery import Battery
import json

battery = Blueprint('battery', __name__)

@battery.route("/battery", methods=["GET", "POST"])
def create_battery():
    return render_template("battery.html", device=session['battery'])

