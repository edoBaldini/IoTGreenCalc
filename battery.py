class Battery:

    TECHNOLOGY = ["Li-Ion", "PbA", "NiMh"]

    MANUFACTURING_ENERGY = {"Li-Ion": 164.8,    # IN MEGAJOULES [MJ]
                            "PbA": 29.175,
                            "NiMh": 204.143}

    DISPOSAL_KG = {"Li-Ion": 0.552,              # IN [KG]
                   "PbA": 0.388,
                   "NiMh": 0.670}

    DENSITY_WH_KG = {"Li-Ion": 140,
                     "PbA": 27,
                     "NiMh": 73}

    EFFICIENCY = {"Li-Ion": 90,
                  "PbA": 80,
                  "NiMh": 66}

    LIFETIME = {"Li-Ion": 15,
                "PbA": 3.85,
                "NiMh": 7.95}

    def __init__(self):
        self.technology = None
        self.lifetime = 0
        self.efficiency = 0
        self.density = 0
        self.capacity = 0
        self.weight = 0
        self.e_manufactoring = 0
        self.disposal = 0

    def compute_e_manufactoring(self):
        self.e_manufactoring = self.weight *\
            self.MANUFACTURING_ENERGY[self.technology]

    def compute_disposal(self):
        self.disposal = self.weight * self.DISPOSAL_KG[self.technology]

    def complete_fields(self):
        self.auto_set_eff() if self.efficiency is None else self.efficiency
        self.auto_set_lifetime() if self.lifetime is None else self.lifetime
        self.auto_set_density() if self.density == 0 else self.density

    def auto_set_eff(self):
        self.efficiency = self.EFFICIENCY[self.technology]

    def auto_set_lifetime(self):
        self.lifetime = self.LIFETIME[self.technology]

    def auto_set_density(self):
        self.density = self.DENSITY_WH_KG[self.technology]
