class Device:

    def __init__(self):
        self.boards = {}
        self.sensors = {}
        self.processor = None
        self.radio = None
        self.active_mode = 0
        self.sleep_mode = 0

    def addSensor(self, s):
        self.sensors[len(self.sensors)] = s

    def addBoard(self, b):
        self.boards[len(self.board)] = b


class Component:

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
        self.MANUFACTURING_ENERGY = 5.74  # needed to put this data in __dict__
        self.e_manufactoring = self.area * self.MANUFACTURING_ENERGY

    # def __init__(self, lifetime, area, active_mode, sleep_mode):
    #    super().__init__(active_mode, sleep_mode)
    #    self.area = area
    #    self.lifetime = lifetime
    #    self.e_manufactoring = self.area * self.MANUFACTURING_ENERGY
