import logging

from flask import request
from flask_restplus import Resource
from iot_green_calculator.api.device_serializer import device_input_fields, device
from iot_green_calculator.api.restplus import api
from iot_green_calculator.device import Device, DeviceError

log = logging.getLogger(__name__)

ns = api.namespace('device', description='Device operations')


@ns.route('/')
class CategoryCollection(Resource):
    @api.marshal_with(device)
    def get(self):
        return {}

    @api.expect(device_input_fields)
    def post(self):
        data = request.json
        try:
            device = Device(data)
        except DeviceError as e:
            print(e.message)
            return e.message, 400
        
        return device.__dict__


