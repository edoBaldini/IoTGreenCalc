class Device:

    def __init__(self):
        self.boards = {}
        self.processor
        self.radio
        self.sensors = {}
        self.active_mode = 0
        self.sleep_mode = 0


class Component:

    def __init__(self, active_mode=0, sleep_mode=0):
        self.active_mode = active_mode
        self.sleep_mode = sleep_mode


class Board(Component):

    DISPOSAL_KG = 0.38

    def __init__(self, weight, active_mode, sleep_mode):
        super().__init__(active_mode, sleep_mode)
        self.weight = weight
        self.disposal = weight * self.DISPOSAL_KG
        self.elements = {}


class Element(Component):

    MANUFACTURING_ENERGY = 5.74

    def __init__(self, lifetime, area, active_mode, sleep_mode):
        super().__init__(active_mode, sleep_mode)
        self.area = area
        self.lifetime = lifetime
        self.e_manufactoring = self.area * self.MANUFACTURING_ENERGY
