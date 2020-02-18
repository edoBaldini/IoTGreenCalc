class Solar_Panel:

    TECHNOLOGY = ["mono-Si", "multi-Si"]  # "CdTe"]

    MANUFACTURING_ENERGY = {"mono-Si": 5195.55,  # IN MEGAJOULES [MJ]
                            "multi-Si": 4047.9}
                           # "CdTe": 3749.16}

    DISPOSAL_KG = {"Si": 0.0447}                 # IN KILOGRAMS [Kg]
                   # "CdTe": 0.0487}

    DENSITY_KG_WP = {"Si": 0.102}
                     # "CdTe": 0.202}

    EFFICIENCY = {"mono-Si": 13,               # DEFINED AS [Kwp / m2]
                  "multi-Si": 12.30}
                  
                  # "CdTe": 10.90}

    WH2MJ = 3600 * 10 ** (- 6)                   # CONVERSION FROM WH TO MJ
    LIFETIME = 43.73

    def __init__(self):
        self.technology = None
        self.surface = 0                   # In [m2]
        self.irradiance = 0            # Daily irradiation [kWh / m2]
        self.s_hours = 0                   # Daily solar hours
        self.lifetime = 0
        self.efficiency = 0
        self.kwp = 0

    def compute_e_manufactoring(self):
        self.e_manufactoring = self.surface *\
            self.MANUFACTURING_ENERGY[self.technology]

    def compute_disposal(self):
        t = 'Si'
        eff = self.efficiency / 100
        self.disposal = eff * self.surface * (10**3) *\
            self.DENSITY_KG_WP[t] * self.DISPOSAL_KG[t]

    def daily_energy_produced(self):
        eff = self.efficiency / 100
        self.e_produced = self.surface * self.irradiance * eff *\
            (10**3) * self.WH2MJ

    def auto_set_eff(self):
        self.efficiency = self.EFFICIENCY[self.technology]
        self.kwp = self.efficiency * self.surface

    def auto_set_lifetime(self):
        self.lifetime = self.LIFETIME

    def complete_fields(self):
        self.auto_set_eff() if self.efficiency is None else self.efficiency
        self.auto_set_lifetime() if self.lifetime is None else self.lifetime
