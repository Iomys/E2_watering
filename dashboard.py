import time

from ubidots import ApiClient
from classes import Measures

class Dashboard:
    API_TOKEN = "BBFF-lyOOKy3EBYeAzaruUbMk0E8mckUCQ9"
    rpi = Measures()

    api = ApiClient(token=API_TOKEN)
    temp_rpi = '60a647851d8472029fed5c66'
    temp_soil = '60a648081d847205570d4f6a'
    hum_rpi = '60a648061d84720586158528'
    hum_soil0 = '60a648091d847205b05a2494'
    hum_soil1 = '60a6480a1d847205e954744f'
    hum_soil2 = '60a6480c1d847205e9547450'
    hum_soil_rel = '60b952e71d84720ed547d39e'

    def __init__(self):
        self.variable_auto_arrosage = self.api.get_variable("60a651eb1d847239ab0118f6")
        self.variable_arrosage_forced = self.api.get_variable("60a651d61d847238a3e72c50")
        self.variable_state = self.api.get_variable("60b954ad1d847219408fe399")

    def publish_sensors(self):
        try:
            self.api.save_collection([{'variable': self.temp_rpi, 'value': self.rpi.aht10_temp()},
                                      # {'variable': self.hum_rpi, 'value':self.rpi.aht10_hum()},
                                      # {'variable': self.hum_soil0, 'value': self.rpi.soil_hum_cap0()},
                                      # {'variable': self.hum_soil1, 'value': self.rpi.soil_hum_cap1()},
                                      # {'variable': self.hum_soil2, 'value': self.rpi.soil_hum_cap2()},
                                      {'variable': self.temp_soil, 'value': self.rpi.ds18b20.get_temperature()},
                                      {'variable': self.hum_soil_rel, 'value': self.rpi.humidity_to_percent(self.rpi.soil_hum_cap2())},
                                      ])
        except:
            pass

    def get_auto_state(self):
        """

        :return:
        """
        value = self.variable_auto_arrosage.get_values(1)[0]['value']
        if value:
            return True
        else:
            return False

    def get_arrosage_state(self):
        """

        :return:
        """
        value = self.variable_arrosage_forced.get_values(1)[0]['value']
        if value:
            return True
        else:
            return False

    def set_auto_state(self, state):
        if state:
            output = 1
        else:
            output = 0
        self.variable_auto_arrosage.save_value({'value': output})

    def set_arrosage_state(self, state):
        if state:
            output = 1
        else:
            output = 0
        self.variable_state.save_value({'value': output})

    def set_arrosage_forced(self, state):
        if state:
            output = 1
        else:
            output = 0
        self.variable_arrosage_forced.save_value({'value': output})


