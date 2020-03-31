class Device:

    default_data = {
        'boards': {},
        'sensors': {},
        'processor': None,
        'radio': None, 
        'active_mode': None,
        'sleep_mode': None,
        'duty_cycle': 0,
        'voltage': 0,
        'daily_e_required': None,
        'e_manufactoring': None,
        'disposal': None, 
        'output_regulator': 0
    }

    def __init__(self, data=default_data):
        self.duty_cycle = data.get('duty_cycle')
        self.voltage = data.get('voltage')
        self.output_regulator = data.get('output_regulator')

        self.device_validation()

        ''' these fields do not need a validation because the validation
            is done in the in the element and board constructor '''
        try:
            self.add_multiple_boards(data.get('boards'))
            self.add_multiple_sensors(data.get('sensors'))
            self.processor = Element(data.get('processor'))
            self.radio = Element(data.get('radio'))
        except (BoardError, ElementError) as e:
            raise DeviceError('error in the provided boards, sensors, radio\
                                or processor')
        
        self.compute_e_manufactoring(self.sensors, self.processor, self.radio)
        self.disposal(self.boards)
        self.compute_e_required(self.duty_cycle, self.active_mode, self.sleep_mode, self.voltage)


    def device_validation(self):
        validation_satus = {}
        validation_satus['duty_cycle'] = self.duty_cycle > 0.0 and self.duty_cycle < 100
        validation_satus['voltage'] = self.voltage > 0.0
        validation_satus['output_regulator'] = self.output_regulator > 0.0 and self.output_regulator < 100.0

        if all(value for value in validation_satus.values()):
            return True
        else:
            raise DeviceError(validation_satus)

    def add_multiple_boards(self, boards):
        self.boards = {}
        for b in boards.values():
            new_board = Board(b)
            self.add_board(new_board)
    
    def add_multiple_sensors(self, sensors):
        self.sensors = {}
        for s in sensors.values():
            new_sensor = Element(s)
            self.add_sensor(new_sensor)

    def add_sensor(self, s):
        self.sensors[len(self.sensors)] = s

    def add_board(self, b):
        self.boards[len(self.boards)] = b

    def compute_e_manufactoring(self, sensors, processor, radio):
        self.e_manufactoring = 0
        for s in sensors.values():
            self.e_manufactoring += s.e_manufactoring
        self.e_manufactoring += processor.e_manufactoring
        self.e_manufactoring += radio.e_manufactoring

    def disposal_dict(self, boards):
        self.disposal = 0
        for b in boards.values():
            self.boards += b.disposal

# Energy required daily in Mj
    def compute_e_required(self, duty_cycle, active_mode, sleep_mode, voltage):
        dc = duty_cycle / 100
        return((dc * active_mode) + ((1 - dc) * sleep_mode)) * 3600 * 24 *\
            voltage * 10 ** (-9)

class DeviceError(Exception):
    def __init__(self, message):
        self.message = message


class Board():

    DISPOSAL_KG = 0.38

    default_data = {
        'weight': 0,
        'active_mode': 0,
        'sleep_mode': 0,
        'disposal': None,
    }

    def __init__(self, data=default_data):
       self.area = data.get('weight')
       self.active_mode = data.get('active_mode')
       self.sleep_mode = data.get('sleep_mode')
       
       self.board_validation()

       self.disposal = self.compute_disposal()
    

    def board_validation(self):
        validation_status = {}
        validation_status['weight'] = self.area > 0
        validation_status['active_mode'] = self.active_mode > 0
        validation_status['sleep_mode'] = self.sleep_mode > 0
        if all(value for value in validation_status.values()):
            return True
        else:
            raise BoardError(validation_status)

    def compute_disposal(self):
        self.DISPOSAL_KG
        self.disposal = self.weight * self.DISPOSAL_KG

class BoardError(Exception):
    def __init__(self, message):
        self.message = message



class Element():

    MANUFACTURING_ENERGY = 5.544

    default_data = {
        'lifetime': 0,
        'area': 0,
        'active_mode': 0,
        'sleep_mode': 0,
        'e_manufacturing': None,
    }

    def __init__(self, data=default_data):
       self.area = data.get('area')
       self.lifetime = data.get('lifetime')
       self.active_mode = data.get('active_mode')
       self.sleep_mode = data.get('sleep_mode')
       
       self.element_validation()

       self.e_manufactoring = self.compute_e_manufactoring()

    def element_validation(self):
        validation_status = {}
        validation_status['area'] = self.area > 0
        validation_status['lifetime'] = self.lifetime > 0
        validation_status['active_mode'] = self.active_mode > 0
        validation_status['sleep_mode'] = self.sleep_mode > 0
        if all(value for value in validation_status.values()):
            return True
        else:
            raise ElementError(validation_status)

    def compute_e_manufactoring(self):
        self.MANUFACTURING_ENERGY  # needed to put this data in __dict__
        self.e_manufactoring = self.area * self.MANUFACTURING_ENERGY

class ElementError(Exception):
    def __init__(self, message):
        self.message = message