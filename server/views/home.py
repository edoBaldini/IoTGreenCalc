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
    # if len(session) == 0:
    #     session['battery'] = None
    #     session['solar_panel'] = None
    #     session['device'] = Device().__dict__
    #     session['maintenance'] = None

    # session['battery'] = json.dumps({
    #                         "technology": "Li-Ion", 
    #                         "lifetime": 9.0, 
    #                         "efficiency": 90.0, 
    #                         "density": 140.516129, 
    #                         "capacity": 6600.0, 
    #                         "weight": 0.155, 
    #                         "e_manufactoring": 25.544, 
    #                         "disposal": 0.08556000000000001
    #                         })
    # session['solar_panel'] = json.dumps({
    #                                         "technology": "mono-Si", 
    #                                         "surface": 0.03744, 
    #                                         "irradiance": 1.127419355, 
    #                                         "s_hours": 9.0, 
    #                                         "lifetime": 20.0, 
    #                                         "efficiency": 17.0, 
    #                                         "kwp": 0, 
    #                                         "efficiency_w": 80.0, 
    #                                         "weight": 0.54, 
    #                                         "disposal": 0.08650800000000002, 
    #                                         "e_manufactoring": 205.02518400000002, 
    #                                         "e_produced": 0.025832875358534402
    #                                     })
    # sensors = {'0': json.dumps({"active_mode": 11.0, "sleep_mode": 0.0, "lifetime": 1000000.0, "area": 13.8, "e_manufactoring": 76.5072}),
    #             '1': json.dumps({"active_mode": 0.006, "sleep_mode": 0.0, "lifetime": 1000000.0, "area": 0.278, "e_manufactoring": 1.541232}),
    #             '2': json.dumps({"active_mode": 0.5, "sleep_mode": 0.0, "lifetime": 1000000.0, "area": 0.283, "e_manufactoring": 1.5689519999999997}),
    #             '3': json.dumps({"active_mode": 0.38, "sleep_mode": 0.0, "lifetime": 1000000.0, "area": 0.976, "e_manufactoring": 5.410944}),
    #             '4': json.dumps({"active_mode": 3.0, "sleep_mode": 0.0, "lifetime": 10.0, "area": 0.665, "e_manufactoring": 3.68676}),
    #             '5': json.dumps({"active_mode": 26.0, "sleep_mode": 0.0, "lifetime": 10.0, "area": 0.636, "e_manufactoring": 3.525984}),
    #             '6': json.dumps({"active_mode": 34.0, "sleep_mode": 0.0, "lifetime": 10.0, "area": 0.636, "e_manufactoring": 3.525984})}
    # boards = {'0': json.dumps({"active_mode": 0.0, "sleep_mode": 0.0, "weight": 0.02, "disposal": 0.0076}),
    #             '1': json.dumps({"active_mode": 0.0, "sleep_mode": 0.0, "weight": 0.02, "disposal": 0.0076})}
    # processor = json.dumps({"active_mode": 9.0, "sleep_mode": 0.062,  "lifetime": 1000000.0, "area": 2.641, "e_manufactoring": 14.641703999999999})
    # radio = json.dumps({ "active_mode": 0.303030303, "sleep_mode": 0.0, "lifetime": 1000000.0, "area": 6.731, "e_manufactoring": 37.316663999999996})

    # session['device'] = {'sensors': sensors, 'boards': boards, 'processor': processor,
    #                     'radio': radio, 'duty_cycle': '5', 'voltage': '3.3',
    #                     'output_regulator': '90', 'disposal': 0.0152, 'e_manufactoring': 147.72542399999998,
    #                     'sleep_mode': 0.062, 'active_mode': 84.189030303, 'daily_e_required': 0.001216992383999568}

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
        print('green ', session['green']['maintenance'])

        e_values = compute_e_values(session)
        e_g_values = compute_e_values(session['green'])

        w_values = compute_w_values(session)
        w_g_values = compute_w_values(session['green'])

        energy_ratio = compute_ratio(e_values, e_g_values)
        waste_ratio = compute_ratio(w_values, w_g_values)
        labels = ["Device", "SolarPanel", "Battery", "Maintenance"]
        return render_template("index.html", device=session['device'],
                               battery=battery,
                               solar_panel=solar_panel,
                               maintenance=session['maintenance'],
                               labels=labels, e_values=e_values,
                               e_g_values=e_g_values, w_values=w_values,
                               w_g_values=w_g_values,
                               energy_ratio=energy_ratio,
                               waste_ratio=waste_ratio)
    else:
        return render_template("index.html",
                               device=session['device'],
                               battery=battery,
                               solar_panel=solar_panel,
                               maintenance=session['maintenance'])


def compute_ratio(real, green):
    tot_real = 0
    tot_green = 0
    for r, g in zip(real, green):
        tot_real += r
        tot_green += g
    return int(tot_real/tot_green)

def compute_e_values(dataset):
    w_device = dataset['device']['e_manufactoring']
    w_device_rounded = round(w_device, 2)
    w_sp = json.loads(dataset['solar_panel'])['e_manufactoring']
    w_sp_rounded = round(w_sp, 2)
    w_b = json.loads(dataset['battery'])['e_manufactoring']
    w_b_rounded = round(w_b, 2)
    w_m = dataset['maintenance']['tot_main_energy']
    w_m_rounded = round(w_m, 2)

    return [w_device_rounded, w_sp_rounded, w_b_rounded, w_m_rounded]


def compute_w_values(dataset):
    w_device = dataset['device']['disposal'] * 1000
    w_device_rounded = round(w_device, 2)
    w_sp = json.loads(dataset['solar_panel'])['disposal'] * 1000
    w_sp_rounded = round(w_sp, 2)
    w_b = json.loads(dataset['battery'])['disposal'] * 1000
    w_b_rounded = round(w_b, 2)
    w_m = dataset['maintenance']['tot_main_disposal'] * 1000
    w_m_rounded = round(w_m, 2)

    return [w_device_rounded, w_sp_rounded, w_b_rounded, w_m_rounded]


def green():
    compute_g_sp()
    compute_g_b()
    compute_g_m()


def compute_g_sp():
    device = session['device']
    battery_eff = json.loads(session['battery'])['efficiency'] / 100
    solar_panel = json.loads(session['solar_panel'])
    solar_panel_eff = solar_panel['efficiency'] / 100
    solar_panel_eff_w = solar_panel['efficiency_w'] / 100
    output_regulator = json.loads(device['output_regulator']) / 100
    # energy in kWh
    daily_e_required = convert_Mj_kWh(device['daily_e_required'])
    g_surface = daily_e_required / (solar_panel_eff *
                                    battery_eff *
                                    solar_panel_eff_w *
                                    output_regulator *
                                    solar_panel['irradiance'])
    g_sp = Solar_Panel()
    g_sp.technology = solar_panel['technology']
    g_sp.irradiance = solar_panel['irradiance']
    g_sp.s_hours = solar_panel['s_hours']
    g_sp.lifetime = solar_panel['lifetime']
    g_sp.efficiency = solar_panel['efficiency']
    g_sp.efficiency_w = solar_panel['efficiency_w']
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
    battery_dens = battery['density']
    output_regulator = json.loads(device['output_regulator']) / 100
    solar_panel = json.loads(session['solar_panel'])
    device_daily_e_mWh = convert_Mj_kWh(device['daily_e_required']) * (10 ** 6)
    g_capacity = (device_daily_e_mWh / (battery_eff * output_regulator))\
        * (1 - (solar_panel['s_hours'] / 24))

    g_weight = (1 / battery_dens) * g_capacity * (10 ** (-3))
    g_battery = Battery()
    g_battery.technology = battery['technology']
    g_battery.lifetime = battery['lifetime']
    g_battery.weight = g_weight
    g_battery.capacity = g_capacity
    g_battery.complete_fields()
    g_battery.compute_disposal()
    g_battery.compute_e_manufactoring()

    b = g_battery.__dict__
    for k in b:
        print(k, ': ', b[k])

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


def inspect_component(component):
    real = json.loads(session[component]) if session[component]\
          is not None else None
    if real:
        for key in real:
            print(key, ': ', real[key], '\n')