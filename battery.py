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

    EFFICIENCY = {"Li-Ion": 0.9,
                  "PbA": 0.8,
                  "NiMh": 0.66}

    MTTF = {"Li-Ion": 15,
            "PbA": 3.85,
            "NiMh": 7.95}

    def __init__(self, technology, weight, efficiency=None, mttf=None):
        self.technology = technology
        self.weight = weight
        self.mttf = (self.MTTF[technology] if mttf is None else mttf)
        self.efficiency = (self.EFFICIENCY[technology] if efficiency is None
                           else efficiency)
        self.e_manufactoring = self.weight *\
            self.MANUFACTURING_ENERGY[self.technology]

        self.disposal = self.weight * self.DISPOSAL_KG[self.technology]
