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
            lifetime_units, e_manuf, disposal = prepare_maintenance()
            # print('life ', lifetime_units)
            # print('e manuf: ', e_manuf)
            # print('disposal ', disposal)
            maintenance_sched(lifetime_units, e_manuf, disposal,
                              maintenance.e_intervention,
                              maintenance.n_devices, maintenance.lifetime)
            session['maintenance'] = json.dumps(maintenance.__dict__)
            return redirect(url_for('home.index'))
    else:
        return render_template("maintenance.html", form=form)
    return redirect(url_for('home.index'))

''' Update the Device removing those sensors that have lifetime smaller than
    application.
    Returns data_for_maint()'''


def prepare_maintenance():
    device = session['device']
    maintenance = json.loads(session['maintenance'])
    spec_sensors = {}
    for key, value in device['sensors'].items():
        value = json.loads(value)
        if value['lifetime'] < maintenance['lifetime']:
            spec_sensors[key] = value
    return data_for_maint(spec_sensors)


''' Updates the energy_manufactoring of the Device removing the energy of those
    sensors contained in the dictionary spac_sensors'''


def update_device_e_manuf(spec_sensors):
    device = session['device']
    for key, value in spec_sensors.items():
        device['e_manufactoring'] -= value['e_manufactoring']
    return device['e_manufactoring']


''' Takes as input a dictionary of sensors and returna a triple with:
    -   a list of the components lifetime
    -   a list of the components energy_manufactoring
    -   a list of the components disposal
    components are sensors, battery, solar_panel and device'''


def data_for_maint(spec_sensors):
    disposal = []
    lifetime = []
    e_manuf = []
    sens_e_manuf = 0
    for key, item in spec_sensors.items():
        lifetime += [item['lifetime']]
        e_manuf += [item['e_manufactoring']]
        sens_e_manuf += item['e_manufactoring']
    for key, value in session.items():
        if key == 'battery' or key == 'solar_panel':
            value = json.loads(value)
            lifetime += [value['lifetime']]
            e_manuf += [value['e_manufactoring']]
            disposal += [value['disposal']]
        if key == 'device':
            e_manuf += [(value['e_manufactoring'] - sens_e_manuf)]
            disposal += [value['disposal']]
            lifetime_dev = 0
            for code, item in session['device'].items():
                try:
                    lifetime_dev = min(lifetime_dev, item['lifetime'])
                except (TypeError, KeyError):
                    lifetime_dev = 10000
            lifetime += [lifetime_dev]
    return (lifetime, e_manuf, disposal)


def maintenance_sched(life_units, e_manuf, disposal, e_int,
                      n_devices, life):
    print('life units: ',life_units)
    print('e manu: ', e_manuf)
    print('disposal: ', disposal)
    print('e_int: ', e_int)
    print('n devices: ', n_devices)
    print('life: ', life)
    life = int(life)
    life_units = [int(item) for item in life_units]

    if(len(disposal) < len(life_units)):
        while len(disposal) < len(life_units):
            disposal.insert(0, 0)
    try:
        m = gp.Model()
        m.ModelSense = GRB.MINIMIZE
        n_unit = len(life_units)
        # Add variables
        x = [[m.addVar(vtype=GRB.BINARY, name="x[%s, %s]" % (i, j))
             for i in range(n_unit)] for j in range(life)]
        e_manuf_t = [[elem for elem in e_manuf] for i in range(life)]

        disposal_t = [[elem for elem in disposal] for i in range(life)]

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

    #    for i in range(N):
    #        for j in range(T):
    #            m.addConstr(x[j][i] == y[j][i], 'c2')

        m.optimize()

    #   Print the time in which there will be the maintenances
    #    for v in m.getVars():
    #        print('%s %g' % (v.varName, v.x)) if v.x > 0 else ''

        for i in range(n_unit):
            r_times = [j for j in range(life) if x[j][i].x >= 0.99]
            print('component replaced: ', i + 1, ' at times ',
                  [1 + r_times[k] for k in range(len(r_times))])
            print("number of replacement ", len(r_times), '\n')

        maintenance_list = [j + 1 for j in range(life) if w[j].x >= 0.99]
        print('\nmaintenances: ', maintenance_list)
        print("number of maintenance ", len(maintenance_list))

        print("\nnumber of solutions ", m.SolCount,
              ' number of Objective functions ', m.NumObj)

    #   Print the objective's values
        for i in range(m.NumObj):
            m.setParam(GRB.Param.ObjNumber, i)
            print('For the objective function: %d' % i)
            for e in range(m.SolCount):
                m.setParam(GRB.Param.SolutionNumber, e)
                print(' %6g' % m.ObjNVal)
            print('')

    except gp.GurobiError as e:
        print('Error code ' + str(e.errno) + ': ' + str(e))

    except AttributeError:
        print('Encountered an attribute error')
