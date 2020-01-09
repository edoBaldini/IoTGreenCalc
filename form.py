import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange


class DutyCycleForm(FlaskForm):
    duty_cycle = f.FloatField(u'Duty cycle of the device',
                              validators=[DataRequired()])
    display = ['duty_cycle']


class ElementForm(FlaskForm):
    active_mode = f.FloatField(u'Energy in active mode',
                               validators=[DataRequired()])
    sleep_mode = f.FloatField(u'Energy in sleep mode',
                              validators=[DataRequired()])
    area = f.FloatField(u'Area of the element in cm2',
                        validators=[DataRequired()])
    lifetime = f.FloatField(u'Estimated lifetime',
                            validators=[DataRequired()])
    display = ['active_mode',
               'sleep_mode',
               'area',
               'lifetime']


class BoardForm(FlaskForm):
    active_mode = f.FloatField(u'Energy in active mode',
                               validators=[DataRequired()])
    sleep_mode = f.FloatField(u'Energy in sleep mode',
                              validators=[DataRequired()])
    weight = f.FloatField(u'weight of the board in kg',
                          validators=[DataRequired()])
    display = ['active_mode',
               'sleep_mode',
               'weight']


class BatteryForm(FlaskForm):
    technology = f.SelectField(u'Select Technology',
                               choices=['Li-Ion', 'PbA', 'NiMh'],
                               validators=[DataRequired()])
    weight = f.DecimalField(u'Weight of the battery in kg',
                            validators=[DataRequired()])
    efficiency = f.DecimalField(u'Efficiecny, not required',
                                validators=[NumberRange(min=0.0, max=1.0)])
    mttf = f.DecimalField(u'estimated lifetime, not required')


class SolarForm(FlaskForm):
    technology = f.SelectField(u'Select Technology',
                               choices=["mono-Si", "multi-Si", "CdTe"],
                               validators=[DataRequired()])
    surface = f.DecimalField(u'Surface of the solar panel in m2',
                             validators=[DataRequired()])
    irradiance = f.DecimalField(u'Daily irradiance in Kwh / m2',
                                validators=[DataRequired()])
    s_hours = f.DecimalField(u'Daily sunny hours',
                             validators=[DataRequired()])
    efficiency = f.DecimalField(u'Efficiecny, not required',
                                validators=[NumberRange(min=0.0, max=1.0)])
    mttf = f.DecimalField(u'estimated lifetime, not required')

