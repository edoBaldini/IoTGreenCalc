import logging

from flask import request
from flask_restplus import Resource
from iot_green_calculator.api.maintenance_serializer import maintenance_input_fields, maintenance
from iot_green_calculator.api.restplus import api
from iot_green_calculator.maintenance import Maintenance, MaintenanceError

log = logging.getLogger(__name__)

ns = api.namespace('maintenance', description='Maintenance operations')


@ns.route('/')
class CategoryCollection(Resource):
    @api.marshal_with(maintenance)
    def get(self):
        return {}

    @api.expect(maintenance_input_fields)
    def post(self):
        data = request.json
        try:
            maintenance = Maintenance(data) # inside the maintenance constructor there is an additional validator
        except MaintenanceError as e:
            print(e.message)
            return e.message, 400
        
        return maintenance.__dict__


