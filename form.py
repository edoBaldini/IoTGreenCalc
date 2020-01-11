import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import (DataRequired, InputRequired, NumberRange,
                                Optional)


class DutyCycleForm(FlaskForm):
    duty_cycle = f.FloatField(u'Duty cycle of the device',
                              validators=[DataRequired(),
                                          NumberRange(min=0.0, max=100.0)])
    voltage = f.FloatField(u'Set the voltage of the device',
                           validators=[DataRequired(),
                                       NumberRange(min=0.0, max=250.0)])
    display = ['duty_cycle', 'voltage']


class ElementForm(FlaskForm):
    active_mode = f.FloatField(u'Energy in active mode',
                               validators=[InputRequired()])
    sleep_mode = f.FloatField(u'Energy in sleep mode',
                              validators=[InputRequired()])
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
                               validators=[InputRequired(),
                                           NumberRange(min=0.0)])
    sleep_mode = f.FloatField(u'Energy in sleep mode',
                              validators=[InputRequired(),
                                          NumberRange(min=0.0)])
    weight = f.FloatField(u'weight of the board in kg',
                          validators=[DataRequired()])
    display = ['active_mode',
               'sleep_mode',
               'weight']


class BatteryForm(FlaskForm):
    technology = f.SelectField(u'Select Technology',
                               choices=[('Li-Ion', 'Li-Ion'), ('PbA', 'PbA'),
                                        ('NiMh', 'NiMh')],
                               validators=[InputRequired()])
    weight = f.FloatField(u'Weight of the battery in kg',
                          validators=[InputRequired(), NumberRange(min=0)])
    efficiency = f.FloatField(u'Efficiecny, optional',
                              validators=[Optional(),
                                          NumberRange(min=0.0, max=100.0)])
    lifetime = f.FloatField(u'estimated lifetime, optional',
                            validators=[Optional(), NumberRange(min=0.0)])
    capacity = f.FloatField(u'capacity in [mAh]',
                            validators=[InputRequired(), NumberRange(min=0)])

    display = ['technology', 'weight', 'efficiency', 'lifetime', 'capacity']


class SolarForm(FlaskForm):
    technology = f.SelectField(u'Select Technology',
                               choices=[("mono-Si", "mono-Si"),
                                        ("multi-Si", "multi-Si"),
                                        ("CdTe", "CdTe")],
                               validators=[DataRequired()])
    surface = f.FloatField(u'Surface of the solar panel in [m2]',
                           validators=[DataRequired(), NumberRange(min=0.0)])
    irradiance = f.FloatField(u'Daily irradiance in [Kwh / m2]',
                              validators=[DataRequired(),
                                          NumberRange(min=0.0)])
    s_hours = f.FloatField(u'Daily sunny hours',
                           validators=[DataRequired(), NumberRange(min=0.0)])
    efficiency = f.FloatField(u'Efficiecny, optional',
                              validators=[Optional(),
                                          NumberRange(min=0.0, max=100.0)])
    lifetime = f.FloatField(u'estimated lifetime, not required',
                            validators=[Optional()])

    display = ['technology', 'surface', 'irradiance', 's_hours', 'efficiency',
               'lifetime']


class MaintenanceForm(FlaskForm):
    avg_distance = f.FloatField(u'Average distance for the intervention in km',
                                validators=[DataRequired(),
                                            NumberRange(min=0.0)])
    avg_fuel_cons = f.FloatField(u'Average fuel needed for 100 km optional',
                                 validators=[Optional(),
                                             NumberRange(min=0.0)])
    conv_factor = f.FloatField(u'Conversion factor from liter of fuel to kWh'
                               'optional', validators=[Optional(),
                                                       NumberRange(min=0.0)])
    n_devices = f.FloatField(u'Number of devices that require maintenance',
                             validators=[DataRequired(),
                                         NumberRange(min=1.0)])
    lifetime = f.FloatField(u'Lifetime of the application',
                            validators=[DataRequired(),
                                        NumberRange(min=1.0)])
    display = ['avg_distance', 'avg_fuel_cons', 'conv_factor', 'n_devices',
               'lifetime']


