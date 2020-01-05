class SolarPanel:

    TECHNOLOGY = ["mono-Si", "multi-Si", "CdTe"]

    MANUFACTURING_ENERGY = {"mono-Si": 5195.55,  # IN MEGAJOULES [MJ]
                            "multi-Si": 4047.9,
                            "CdTe": 3749.16}

    DISPOSAL_KG = {"Si": 0.0447,                 # IN KILOGRAMS [Kg]
                   "CdTe": 0.0487}

    DENSITY_KG_WP = {"Si": 0.102,
                     "CdTe": 0.202}

    EFFICIENCY = {"mono-Si": 0.13,               # DEFINED AS [Kwp / m2]
                  "multi-Si": 0.1230,
                  "CdTe": 0.1090}

    WH2MJ = 3600 * 10 ** (- 6)                   # CONVERSION FROM WH TO MJ

    def __init__(self, technology, surface, irradiance, s_hours,
                 efficiency=None, mttf=43.73):
        self.technology = technology
        self.surface = surface                   # In [m2]
        self.irradiance = irradiance             # Daily irradiation [Kw / m2]
        self.s_hours = s_hours                   # Daily solar hours
        self.mttf = mttf
        self.efficiency = (self.EFFICIENCY[technology] if efficiency is None
                           else efficiency)
        self.e_manufactoring = self.surface *\
            self.MANUFACTURING_ENERGY[self.technology]

        t = self.technology if self.technology == 'CdTe' else 'Si'

        self.disposal = self.efficiency * self.surface * (10**3) *\
            self.DENSITY_KG_WP[t] * self.DISPOSAL_KG[t]

        self.e_produced = self.surface * self.irradiance * self.efficiency *\
            (10**3) * self.WH2MJ
