from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import ElementForm, BoardForm, DutyCycleForm
from device import Element, Board, Device
import json

device = Blueprint('device', __name__)


@device.route("/#device", methods=["GET", "POST"])
def create_device():
    device = session['device']
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         duty_cycle = request.form['duty_cycle']
    #         voltage = request.form['voltage']
    #         device['duty_cycle'] = duty_cycle
    #         device['voltage'] = voltage
    if device:
        device['daily_e_required'] = Device.compute_e_required(
            float(device['duty_cycle']),
            float(device['active_mode']),
            float(device['sleep_mode']),
            float(device['voltage']))
    else:
        new_device = Device()
        new_device = json.dumps(new_device.__dict__)
        session['device'] = new_device
    #device['e_manufactoring'] = Device.e_manuf_dict(device['sensors'],
    #                                                device['processor'],
    #                                                device['radio'])
    #device['disposal'] = Device.disposal_dict(device['boards'])
    session['device'] = device
    return render_template("index.html", title_form='Device', device_bool=1)


def update_device(component_name, component, index_component=-1):
    device = session['device']
    component_encoded = json.dumps(component.__dict__)
    if component_name == 'sensors' or component_name == 'boards':
        index_component = str(len(device[component_name])) + 1 if\
            index_component == -1 else str(index_component)
        device[component_name][index_component] = component_encoded
    else:
        device[component_name] = component_encoded
    device['active_mode'] += component.active_mode
    device['sleep_mode'] += component.sleep_mode

    if component_name == 'boards':
        device['disposal'] += component.disposal
    else:
        device['e_manufactoring'] += component.e_manufactoring

    session['device'] = device


@device.route("/#sensor", methods=["GET", "POST"])
def sensor():
    if 'device' in session:
        form = ElementForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                new_elem = Element()
                form.populate_obj(new_elem)
                new_elem.compute_e_manufactoring()
                update_device('sensors', new_elem)
                return redirect(url_for('device.create_device'))
    else:
        return redirect(url_for('.index'))
    return render_template("element.html", form=form)


@device.route("/#board", methods=["GET", "POST"])
def board():
    form = BoardForm()
    boards = session['device']['boards']
    forms = [BoardForm() for i in boards]
    r_form = forms if len(boards) > 0 else [form]
    if request.method == 'POST':
        if form.validate_on_submit():
            if request.form.get('delete', None):
                session.modified = True
                del session['device']['boards'][request.form.get('delete', None)]
            else:
                new_element = Board()
                form.populate_obj(new_element)
                new_element.compute_disposal()
                index = int(request.form.get('submit')) if\
                    request.form.get('submit') else -1
                update_device('boards', new_element, index)
            return redirect(url_for('device.create_device'))

        if request.form.get('add', None) == 'add':
            board = Board()
            board_encoded = json.dumps(board.__dict__)
            index = len(session['device']['boards'])
            session.modified = True
            session['device']['boards'][str(index)] = board_encoded
            return redirect(url_for('device.board'))

    elif session['device']['boards']:
        for f, p_m in zip(forms, boards):
            board = json.loads(boards[p_m])
            for e, key in zip(f, board):
                e.data = board[key]
    return render_template("index.html", device_bool=1, title_form='Boards',
                           form=r_form)


@device.route("/#processor", methods=["GET", "POST"])
def processor():
    form = ElementForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            new_element = Element()
            form.populate_obj(new_element)
            new_element.compute_e_manufactoring()
            update_device('processor', new_element)
            return redirect(url_for('device.create_device'))

    elif session['device']['processor']:
        processor = json.loads(session['device']['processor'])
        for e, key in zip(form, processor):
            e.data = processor[key]
    return render_template("index.html", device_bool=1, title_form='Processor',
                           form=form)


@device.route("/#radio", methods=["GET", "POST"])
def radio():
    form = ElementForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_element = Element()
            form.populate_obj(new_element)
            new_element.compute_e_manufactoring()
            update_device('radio', new_element)
            return redirect(url_for('device.create_device'))

    elif session['device']['radio']:
        radio = json.loads(session['device']['radio'])
        for e, key in zip(form, radio):
            e.data = radio[key]
    return render_template("index.html", device_bool=1, title_form='Radio',
                           form=form)


@device.route("/#configuration", methods=["GET", "POST"])
def configuration():
    form = DutyCycleForm()
    if request.method == 'POST':
        device = session['device']
        if form.validate_on_submit():
            duty_cycle = request.form['duty_cycle']
            voltage = request.form['voltage']
            session.modified = True
            session['device']['duty_cycle'] = duty_cycle
            session['device']['voltage'] = voltage
            return redirect(url_for('device.create_device'))
    elif session['device']:
        device = session['device']
        form.duty_cycle.data = device['duty_cycle']
        form.voltage.data = device['voltage']
    return render_template("index.html", device_bool=1, title_form='Configuration', form=form)




