from flask_restplus import fields
from iot_green_calculator.api.restplus import api
from iot_green_calculator.api.battery_serializer import battery
from iot_green_calculator.api.solar_panel_serializer import solar_panel
from iot_green_calculator.api.device_serializer import device, element

maintenance_input_fields = api.model('Maintenance input fields', {
    'avg_distance': fields.Float(required=True, description='Average distance needed to\
                                                            reach the deployment place'),
    'avg_fuel_cons': fields.Float(description='Average fuel consumption'),
    'conv_factor': fields.Float(description='Conversion factor from liter of fuel to kWh'),
    'n_devices': fields.Float(description='Number of devices used in the solution'),
    'lifetime': fields.Float(required=True, description='Application lifetime'),
    'battery': fields.Nested(battery),
    'solar_panel': fields.Nested(solar_panel),
    'device': fields.Nested(device),
})

maintenance = api.inherit('Maintenance', maintenance_input_fields, {
    'e_intervention': fields.Float(description='Energy spent\
                                for one intervention in Mj'),
    'sensors': fields.List(fields.Nested(element)),
    'tot_e_intervention': fields.Float(description='Total energy spent for the \
                                interventions in Mj'),
    'n_interventions': fields.Float(description='Number of interventions'),
    'tot_main_energy': fields.Float(description='Total energy spent for the \
                                maintenance in Mj'),
    'tot_main_disposal': fields.Float(description='Total kg of waste produced\
                                by the maintenance disposal'),
})
