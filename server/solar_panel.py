class Solar_Panel:

    TECHNOLOGY = ["mono-Si", "multi-Si"]  # "CdTe"]

    MANUFACTURING_ENERGY = {"mono-Si": 5476.100,  # IN MEGAJOULES [MJ]
                            "multi-Si": 4676.100}
                           # "CdTe": 3749.16}

    DISPOSAL_KG = {"Si": 0.1602}                 # IN KILOGRAMS [Kg]
                   # "CdTe": 0.0487}

    DENSITY_KG_WP = {"Si": 0.102}
                     # "CdTe": 0.202}

    EFFICIENCY = {"mono-Si": 17,               # DEFINED AS [Kwp / m2]
                  "multi-Si": 12.30}
                  
                  # "CdTe": 10.90}
    EFFICIENCY_W = {"mono-Si": 80,
                    "multi-Si": 80}

    WH2MJ = 3600 * 10 ** (- 6)                   # CONVERSION FROM WH TO MJ
    LIFETIME = 43.73

    default_data = {
        'technology': None,
        'surface': 0,                           # squared meters
        'irradiance': 0,                        # 
        's_hours': 0,
        'lifetime': 0,                          # years   
        'efficiency': 0,                        
        'kwp': 0,
        'efficiency_w': 0,                      # wear-out efficiency
        'weight': 0                             # kg
    }
    
    def __init__(self,data=default_data):
        self.technology = data.get('technology')
        self.surface = data.get('surface')
        self.irradiance = data.get('irradiance')
        self.s_hours = data.get('s_hours')
        self.lifetime = data.get('lifetime')
        self.efficiency = data.get('efficiency')
        self.kwp = data.get('kwp')
        self.efficiency_w = data.get('efficiency_w')
        self.weight = data.get('weight')

    def compute_e_manufactoring(self):
        self.e_manufactoring = self.surface *\
            self.MANUFACTURING_ENERGY[self.technology]

    def compute_disposal(self):
        t = 'Si'
        eff = self.efficiency / 100
        if self.weight == 0:
            self.disposal = eff * self.surface * (10**3) *\
            self.DENSITY_KG_WP[t] * self.DISPOSAL_KG[t]
        else:
            self.disposal = self.weight * self.DISPOSAL_KG[t]

    def daily_energy_produced(self):
        eff = self.efficiency / 100
        self.e_produced = self.surface * self.irradiance * eff *\
            (10**3) * self.WH2MJ

    def auto_set_eff(self):
        self.efficiency = self.EFFICIENCY[self.technology]
        self.kwp = self.efficiency * self.surface
        self.efficiency_w = self.EFFICIENCY[self.technology]

    def auto_set_lifetime(self):
        self.lifetime = self.LIFETIME

    def complete_fields(self):
        self.auto_set_eff() if self.efficiency is None else self.efficiency
        self.auto_set_lifetime() if self.lifetime is None else self.lifetime
