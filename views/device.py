from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import ElementForm, BoardForm, DutyCycleForm
from device import Element, Board, Device
import json

device = Blueprint('device', __name__)


@device.route("/device", methods=["GET", "POST"])
def create_device():
    form = DutyCycleForm()
    device = session['device']
    if request.method == 'POST':
        if form.validate_on_submit():
            duty_cycle = request.form['duty_cycle']
            voltage = request.form['voltage']
            device['duty_cycle'] = duty_cycle
            device['voltage'] = voltage

    device['daily_e_required'] = Device.compute_e_required(
        float(device['duty_cycle']),
        float(device['active_mode']),
        float(device['sleep_mode']),
        float(device['voltage']))
    session['device'] = device
    return render_template("device.html", form=form, device=session['device'])


def update_device(component_name, component):
    device = session['device']
    component_encoded = json.dumps(component.__dict__)
    if component_name == 'sensors' or component_name == 'boards':
        index_component = str(len(device[component_name]))
        device[component_name][index_component] = component_encoded
    else:
        device[component_name] = component_encoded
    device['active_mode'] += component.active_mode
    device['sleep_mode'] += component.sleep_mode
    session['device'] = device


@device.route("/sensor", methods=["GET", "POST"])
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
    return render_template("sensor.html", form=form)


@device.route("/board", methods=["GET", "POST"])
def board():
    form = BoardForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_element = Board()
            form.populate_obj(new_element)
            new_element.compute_disposal()
            update_device('boards', new_element)
            return redirect(url_for('device.create_device'))
    return render_template("board.html", form=form)


@device.route("/processor", methods=["GET", "POST"])
def processor():
    form = ElementForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_element = Element()
            form.populate_obj(new_element)
            new_element.compute_e_manufactoring()
            update_device('processor', new_element)
            return redirect(url_for('device.create_device'))
    return render_template("processor.html", form=form)


@device.route("/radio", methods=["GET", "POST"])
def radio():
    form = ElementForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_element = Element()
            form.populate_obj(new_element)
            new_element.compute_e_manufactoring()
            update_device('radio', new_element)
            return redirect(url_for('device.create_device'))
    return render_template("radio.html", form=form)

