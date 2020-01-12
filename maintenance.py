class Maintenance:

    kwh_to_Mj = 3600 * (10 ** (-3))

    def __init__(self):
        self.avg_distance = 0
        self.avg_fuel_cons = 5
        self.conv_factor = 9.2
        self.n_devices = 0
        self.lifetime = 0
        self.e_intervention = 0
        self.battery = {}
        self.solar_panel = {}
        self.sensors = {}
        self.tot_e_intervention = 0
        self.n_interventions = 0
        self.tot_main_energy = 0
        self.tot_main_disposal = 0

    def update_e_intervention(self):
        self.e_intervention = (self.avg_distance * self.avg_fuel_cons) / 100 *\
            self.conv_factor * self.kwh_to_Mj
