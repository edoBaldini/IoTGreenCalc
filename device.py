class Device:

    def __init__(self):
        self.boards = {}
        self.sensors = {}
        self.processor = None
        self.radio = None
        self.active_mode = 0
        self.sleep_mode = 0
        self.duty_cycle = 0
        self.voltage = 0
        self.daily_e_required = 0
        self.e_manufactoring = 0
        self.disposal = 0

    def add_sensor(self, s):
        self.sensors[len(self.sensors)] = s

    def add_board(self, b):
        self.boards[len(self.board)] = b

    def e_manuf_dict(sensors, processor, radio):
        e_manufactoring = 0
        for key in sensors:
            e_manufactoring += sensors[key]['e_manufactoring']
        e_manufactoring += processor['e_manufactoring']
        e_manufactoring += radio['e_manufactoring']
        return e_manufactoring

    def disposal_dict(boards):
        disposal = 0
        for key in boards:
            boards += boards[key]['disposal']
        return disposal

# Energy required daily in Mj
    def compute_e_required(duty_cycle, active_mode, sleep_mode, voltage):
        dc = duty_cycle / 100
        return((dc * active_mode) + ((1 - dc) * sleep_mode)) * 3600 * 24 *\
            voltage * 10 ** (-9)


class Component:

    # Active and sleep mode in [mA]
    def __init__(self, active_mode=0, sleep_mode=0):
        self.active_mode = active_mode
        self.sleep_mode = sleep_mode


class Board(Component):

    DISPOSAL_KG = 0.38
    weight = 0
    active_mode = 0
    sleep_mode = 0
    disposal = None

    def compute_disposal(self):
        self.DISPOSAL_KG
        self.disposal = self.weight * self.DISPOSAL_KG

    # def __init__(self, weight, active_mode, sleep_mode):
    #    super().__init__(active_mode, sleep_mode)
    #    self.weight = weight
    #    self.disposal = weight * self.DISPOSAL_KG
    #    self.elements = {}


class Element(Component):

    MANUFACTURING_ENERGY = 5.74
    lifetime = 0
    area = 0
    active_mode = 0
    sleep_mode = 0
    e_manufactoring = None

    def compute_e_manufactoring(self):
        self.MANUFACTURING_ENERGY  # = 5.74 needed to put this data in __dict__
        self.e_manufactoring = self.area * self.MANUFACTURING_ENERGY

    # def __init__(self, lifetime, area, active_mode, sleep_mode):
    #    super().__init__(active_mode, sleep_mode)
    #    self.area = area
    #    self.lifetime = lifetime
    #    self.e_manufactoring = self.area * self.MANUFACTURING_ENERGY
