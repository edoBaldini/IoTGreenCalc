from flask import (Blueprint, render_template, request, session, redirect,
                   url_for)
from device import Device
from battery import Battery
from solar_panel import Solar_Panel
from maintenance import Maintenance
import json
from .maintenance import prepare_maintenance, maintenance_sched
home = Blueprint('home', __name__)

@home.route('/', methods=["GET", "POST"])
def index():
    if len(session) == 0:
        session['battery'] = None
        session['solar_panel'] = None
        session['device'] = Device().__dict__
        session['maintenance'] = None

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

        # create the maintenance
        if request.form.get('maintenance', None) == 'Maintenance':
            return redirect(url_for('maintenance.create_maintenance'))

        # pressed delete button
        if request.form.get('battery', None) == 'delete':
            session['battery'] = None
            session['maintenance'] = None
        if request.form.get('solar_panel', None) == 'delete':
            session['solar_panel'] = None
            session['maintenance'] = None
        if request.form.get('device', None) == 'delete':
            session['device'] = None
            session['maintenance'] = None
        if request.form.get('maintenance', None) == 'delete':
            session['maintenance'] = None

    battery = json.loads(session['battery']) if session['battery']\
        is not None else None
    solar_panel = json.loads(session['solar_panel']) if\
        session['solar_panel'] is not None else None

    if session['maintenance']:
        green()
        g_battery = json.loads(session['green']['battery'])
        g_sp = json.loads(session['green']['solar_panel'])
        return render_template("index.html", device=session['device'],
                               battery=battery,
                               solar_panel=solar_panel,
                               maintenance=session['maintenance'],
                               g_battery=g_battery,
                               g_sp=g_sp,
                               g_main=session['green']['maintenance'])
    else:
        return render_template("index.html", device=session['device'],
                               battery=battery,
                               solar_panel=solar_panel,
                               maintenance=session['maintenance'])


def green():
    compute_g_sp()
    compute_g_b()
    compute_g_m()


def compute_g_sp():
    device = session['device']
    battery_eff = json.loads(session['battery'])['efficiency'] / 100
    solar_panel = json.loads(session['solar_panel'])
    solar_panel_eff = solar_panel['efficiency'] / 100
    # energy in kWh
    daily_e_required = convert_Mj_kWh(device['daily_e_required'])
    g_surface = daily_e_required / (solar_panel_eff *
                                    battery_eff *
                                    solar_panel['irradiance'])
    g_sp = Solar_Panel()
    g_sp.technology = solar_panel['technology']
    g_sp.irradiance = solar_panel['irradiance']
    g_sp.s_hours = solar_panel['s_hours']
    g_sp.lifetime = solar_panel['lifetime']
    g_sp.efficiency = solar_panel['efficiency']
    g_sp.surface = g_surface
    g_sp.daily_energy_produced()
    g_sp.compute_disposal()
    g_sp.compute_e_manufactoring()
    session['green'] = {}
    session['green']['device'] = device
    session['green']['solar_panel'] = json.dumps(g_sp.__dict__)


def compute_g_b():
    device = session['device']
    battery = json.loads(session['battery'])
    battery_eff = battery['efficiency'] / 100
    solar_panel = json.loads(session['solar_panel'])
    device_daily_e_mWh = convert_Mj_kWh(device['daily_e_required']) * (10 ** 6)
    g_capacity = (device_daily_e_mWh /
                  battery_eff) * (1 - (solar_panel['s_hours'] / 24))

    g_weight = (1 / battery['density']) * g_capacity * (10 ** (-3))
    g_battery = Battery()
    g_battery.technology = battery['technology']
    g_battery.weight = g_weight
    g_battery.capacity = g_capacity
    g_battery.complete_fields()
    g_battery.compute_disposal()
    g_battery.compute_e_manufactoring()

    session['green']['battery'] = json.dumps(g_battery.__dict__)


def compute_g_m():
    maintenance = session['maintenance']
    g_maintenance = Maintenance()
    g_maintenance.avg_distance = maintenance['avg_distance']
    g_maintenance.avg_fuel_cons = maintenance['avg_fuel_cons']
    g_maintenance.conv_factor = maintenance['conv_factor']
    g_maintenance.n_devices = maintenance['n_devices']
    g_maintenance.lifetime = maintenance['lifetime']
    g_maintenance.e_intervention = maintenance['e_intervention']
    session['green']['maintenance'] = json.dumps(g_maintenance.__dict__)
    g_dataset = session['green']
    lifetime_units, e_manuf, disposal = prepare_maintenance(g_dataset)
    g_m_session = maintenance_sched(lifetime_units, e_manuf, disposal,
                                    g_maintenance.__dict__)

    session['green']['maintenance'] = g_m_session


def convert_Mj_kWh(value_Mj):
    return (value_Mj * (10 ** 3) / 3600)


