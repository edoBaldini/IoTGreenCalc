class Battery:

    TECHNOLOGY = ["Li-Ion", "PbA", "NiMh"]

    MANUFACTURING_ENERGY = {"Li-Ion": 129.87,    # IN MEGAJOULES [MJ]
                            "PbA": 27.25,
                            "NiMh": 127.52}

    DISPOSAL_KG = {"Li-Ion": 0.508,              # IN [KG]
                   "PbA": 0.676,
                   "NiMh": 0.682}

    DENSITY_WH_KG = {"Li-Ion": 140,
                     "PbA": 27,
                     "NiMh": 73}

    EFFICIENCY = {"Li-Ion": 90,
                  "PbA": 80,
                  "NiMh": 66}

    MTTF = {"Li-Ion": 15,
            "PbA": 3.85,
            "NiMh": 7.95}

    def __init__(self):
        self.technology = None
        self.mttf = 0
        self.efficiency = 0
        self.capacity = 0
        self.e_manufactoring = 0
        self.weight = 0
        self.disposal = 0


    def compute_e_manufactoring(self):
        self.e_manufactoring = self.weight *\
            self.MANUFACTURING_ENERGY[self.technology]

    def compute_disposal(self):
        self.disposal = self.weight * self.DISPOSAL_KG[self.technology]

    def auto_set_eff(self):
        self.efficiency = self.EFFICIENCY[self.technology]

    def auto_set_mttf(self):
        self.mttf = self.MTTF[self.technology]
