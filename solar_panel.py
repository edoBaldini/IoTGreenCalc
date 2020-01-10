class Solar_Panel:

    TECHNOLOGY = ["mono-Si", "multi-Si", "CdTe"]

    MANUFACTURING_ENERGY = {"mono-Si": 5195.55,  # IN MEGAJOULES [MJ]
                            "multi-Si": 4047.9,
                            "CdTe": 3749.16}

    DISPOSAL_KG = {"Si": 0.0447,                 # IN KILOGRAMS [Kg]
                   "CdTe": 0.0487}

    DENSITY_KG_WP = {"Si": 0.102,
                     "CdTe": 0.202}

    EFFICIENCY = {"mono-Si": 13,               # DEFINED AS [Kwp / m2]
                  "multi-Si": 12.30,
                  "CdTe": 10.90}

    WH2MJ = 3600 * 10 ** (- 6)                   # CONVERSION FROM WH TO MJ

    def __init__(self):
        self.technology = None
        self.surface = 0                   # In [m2]
        self.irradiance = 0            # Daily irradiation [Kwh / m2]
        self.s_hours = 0                   # Daily solar hours
        self.mttf = 43.73

    def compute_e_manufactoring(self):
        self.e_manufactoring = self.surface *\
            self.MANUFACTURING_ENERGY[self.technology]

    def compute_disposal(self):
        t = self.technology if self.technology == 'CdTe' else 'Si'
        eff = self.efficiency / 100
        self.disposal = eff * self.surface * (10**3) *\
            self.DENSITY_KG_WP[t] * self.DISPOSAL_KG[t]

    def daily_energy_produced(self):
        eff = self.efficiency / 100
        self.e_produced = self.surface * self.irradiance * eff *\
            (10**3) * self.WH2MJ

    def auto_set_eff(self):
        self.efficiency = self.EFFICIENCY[self.technology]
