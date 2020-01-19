import gurobipy as gp
from gurobipy import GRB, quicksum
from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import MaintenanceForm
from maintenance import Maintenance
import json

maintenance = Blueprint('maintenance', __name__)


@maintenance.route("/maintenance", methods=["GET", "POST"])
def create_maintenance():
    form = MaintenanceForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            maintenance = Maintenance()
            form.populate_obj(maintenance)
            maintenance.update_e_intervention()
            session['maintenance'] = json.dumps(maintenance.__dict__)

            dataset = session
            lifetime_units, e_manuf, disposal = prepare_maintenance(dataset)
            session['maintenance'] = json.dumps(maintenance.__dict__)
            m_session = maintenance_sched(lifetime_units, e_manuf, disposal,
                                          maintenance.__dict__)
            session['maintenance'] = m_session
            return redirect(url_for('home.index'))
    else:
        return render_template("element.html", form=form)
    return redirect(url_for('home.index'))


''' Update the Device removing those sensors that have lifetime smaller than
    application.
    Returns data_for_maint()'''


def prepare_maintenance(dataset):
    device = dataset['device']
    maintenance = json.loads(dataset['maintenance'])
    spec_sensors = {}
    for key, value in device['sensors'].items():
        value = json.loads(value)
        if value['lifetime'] < maintenance['lifetime']:
            spec_sensors[key] = value
    return data_for_maint(spec_sensors, dataset)


''' Takes as input a dictionary of sensors and returna a triple with:
    -   a list of the components lifetime
    -   a list of the components energy_manufactoring
    -   a list of the components disposal
    components are sensors, battery, solar_panel and device'''


def data_for_maint(spec_sensors, dataset):
    disposal = {}
    lifetime = {}
    e_manuf = {}
    sens_e_manuf = 0
    for key, item in spec_sensors.items():
        lifetime[len(lifetime)] = item['lifetime']
        e_manuf[len(lifetime)] = item['e_manufactoring']
        sens_e_manuf += item['e_manufactoring']
    for key, value in dataset.items():
        if key == 'battery' or key == 'solar_panel':
            value = json.loads(value)
            lifetime[key] = value['lifetime']
            e_manuf[key] = value['e_manufactoring']
            disposal[key] = value['disposal']
        if key == 'device':
            e_manuf[key] = (value['e_manufactoring'] - sens_e_manuf)
            disposal[key] = value['disposal']
            lifetime_dev = 0
            for code, item in dataset['device'].items():
                try:
                    lifetime_dev = min(lifetime_dev, item['lifetime'])
                except (TypeError, KeyError):
                    lifetime_dev = 10000
            lifetime[key] = lifetime_dev
    return (lifetime, e_manuf, disposal)


def update_maintenance(n_maintenance, e_manuf, disposal):
    key_maintenance = {'n_maintenance': n_maintenance,
                       'e_maintenance': n_maintenance * e_manuf,
                       'd_maintenance': n_maintenance * disposal}
    return json.dumps(key_maintenance)


def maintenance_sched(life_units, e_manuf, disposal, maintenance_session):

    life = int(maintenance_session['lifetime'])
    n_devices = maintenance_session['n_devices']
    e_int = maintenance_session['e_intervention']
    print("lifeunits, ", life_units)
    life_units = [int(item) for key, item in life_units.items()]  # list
    up_disposal = {}
    if len(disposal) < (len(e_manuf) - len(up_disposal)):
        for key, value in e_manuf.items():
            if key not in disposal:
                up_disposal[key] = 0
    for key in disposal:
        up_disposal[key] = disposal[key]

    print('life units: ', life_units)
    print('e manu: ', e_manuf)
    print('e_int: ', e_int)
    print('n devices: ', n_devices)
    print('life: ', life)
    print('disposal: ', up_disposal)

    try:
        m = gp.Model()
        m.ModelSense = GRB.MINIMIZE
        n_unit = len(life_units)
        # Add variables
        x = [[m.addVar(vtype=GRB.BINARY, name="x[%s, %s]" % (i, j))
             for i in range(n_unit)] for j in range(life)]
        e_manuf_t = [[elem for key, elem in e_manuf.items()]
                     for i in range(life)]

        disposal_t = [[elem for key, elem in up_disposal.items()]
                      for i in range(life)]

        w = [m.addVar(vtype=GRB.BINARY, name="w[%s]" % i) for i in range(life)]
        e_int_t = [e_int for i in range(life)]

        # Objective function
        energy_objective = quicksum(quicksum(n_devices * (e_manuf_t[i][j] *
                                             x[i][j]) for j in range(n_unit)) +
                                    (e_int_t[i] * w[i]) for i in range(life))
        disposal_objective = quicksum(quicksum(n_devices * (disposal_t[i][j] *
                                               x[i][j]) for j in range(n_unit))
                                      for i in range(life))

        m.setObjectiveN(energy_objective, 0)
        m.setObjectiveN(disposal_objective, 1)

        # Constraints
        for i in range(n_unit):
            for k in range(life - life_units[i]):
                m.addConstr(quicksum(x[j][i] for j in range(k, k +
                            life_units[i])) >= 1, 'c0')

            for j in range(life):
                m.addConstr(x[j][i] <= w[j], 'c1')

        m.optimize()

        for i in range(n_unit):
            r_times = [j for j in range(life) if x[j][i].x >= 0.99]
            key = list(e_manuf.keys())[i]
            if key == 'battery' or key == 'solar_panel' or key == 'device':
                maintenance_session[key] = update_maintenance(len(r_times),
                                                              e_manuf[key],
                                                              up_disposal[key])
            else:
                maintenance_session['sensors'][key] =\
                    update_maintenance(len(r_times), e_manuf[key],
                                       up_disposal[key])

        maintenance_list = [j + 1 for j in range(life) if w[j].x >= 0.99]
        maintenance_session['n_interventions'] = len(maintenance_list)
        maintenance_session['tot_e_intervention'] = len(maintenance_list) *\
            e_int

        m.setParam(GRB.Param.ObjNumber, 0)
        m.setParam(GRB.Param.SolutionNumber, 0)
        maintenance_session['tot_main_energy'] = (m.ObjNVal / n_devices)

        m.setParam(GRB.Param.ObjNumber, 1)
        m.setParam(GRB.Param.SolutionNumber, 0)
        maintenance_session['tot_main_disposal'] = (m.ObjNVal / n_devices)

        return maintenance_session
    except gp.GurobiError as e:
        print('Error code ' + str(e.errno) + ': ' + str(e))

    except AttributeError:
        print('Encountered an attribute error')
