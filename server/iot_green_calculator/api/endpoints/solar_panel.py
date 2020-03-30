import logging

from flask import request
from flask_restplus import Resource
from iot_green_calculator.api.serializers import solar_panel_input_fields, solar_panel
from iot_green_calculator.api.restplus import api
from iot_green_calculator.solar_panel import Solar_Panel

log = logging.getLogger(__name__)

ns = api.namespace('solar_panel', description='Solar panel operations')


@ns.route('/')
class CategoryCollection(Resource):
    @api.marshal_with(solar_panel)
    def get(self):
        """
        Returns a category with a list of posts.
        """
        return {}

    @api.expect(solar_panel_input_fields)
    def post(self):
        data = request.json
        solar_panel = Solar_Panel(data)
        solar_panel.complete_fields()
        solar_panel.compute_disposal()
        solar_panel.compute_e_manufactoring()
        solar_panel.daily_energy_produced()
        return solar_panel
