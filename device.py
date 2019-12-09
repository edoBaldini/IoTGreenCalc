class Device:

    MANUFACTURING_ENERGY = 5.74

    DISPOSAL_KG = 0.38

    def __init__(self, surface_components, weight_board, mttf, energy_req):
        self.surface_components = surface_components
        self.weight_board = weight_board
        self.mttf = mttf
        self.energy_req = energy_req

    def sp_man_energy(self):
        s = sum(self.surface_components)
        return s * self. MANUFACTURING_ENERGY

    def sp_disposal(self):
        return self.weight_board * self.DISPOSAL_KG
