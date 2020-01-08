from flask import (Blueprint, render_template, request, redirect, url_for,
                   session)
from form import ElementForm, BoardForm
from device import Element, Board
import json
home = Blueprint('home', __name__)


@home.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


@home.route("/device", methods=["GET", "POST"])
def device():
    if 'sensor' in session:
        print(session['sensor'])
    if 'board' in session:
        print(session['board'])
    return render_template("device.html")


@home.route("/sensor", methods=["GET", "POST"])
def sensor():
    form = ElementForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_element = Element()
            form.populate_obj(new_element)
            new_element.compute_e_manufactoring()
            session['sensor'] = json.dumps(new_element.__dict__)
            return redirect(url_for('.device'))
    return render_template("sensor.html", form=form)


@home.route("/board", methods=["GET", "POST"])
def board():
    form = BoardForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_element = Board()
            form.populate_obj(new_element)
            new_element.compute_disposal()
            session['board'] = json.dumps(new_element.__dict__)
            return redirect(url_for('.device'))
    return render_template("board.html", form=form)


@home.route("/processor", methods=["GET", "POST"])
def processor():
    form = ElementForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_element = Element()
            form.populate_obj(new_element)
            new_element.compute_e_manufactoring()
            session['processor'] = json.dumps(new_element.__dict__)
            return redirect(url_for('.device'))
    return render_template("processor.html", form=form)


@home.route("/radio", methods=["GET", "POST"])
def radio():
    form = ElementForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_element = Element()
            form.populate_obj(new_element)
            new_element.compute_e_manufactoring()
            session['radio'] = json.dumps(new_element.__dict__)
            return redirect(url_for('.device'))
    return render_template("radio.html", form=form)


@home.route("/about")
def about():
    return render_template("about.html")

