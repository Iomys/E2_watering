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
    hum_soil1 ='60a6480a1d847205e954744f'
    hum_soil2 = '60a6480c1d847205e9547450'

    def __init__(self):
        self.variable_auto_arrosage = self.api.get_variable("60a651eb1d847239ab0118f6")
        self.variable_arrosage_mnt = self.api.get_variable("60a651d61d847238a3e72c50")

    def publish_sensors(self):
        self.api.save_collection([{'variable': self.temp_rpi, 'value': self.rpi.aht10_temp()},
                                  {'variable': self.hum_rpi, 'value':self.rpi.aht10_hum()},
                                  {'variable': self.hum_soil0, 'value': self.rpi.soil_hum_chin()},
                                  {'variable': self.hum_soil1, 'value': self.rpi.soil_hum_cap1()},
                                  {'variable': self.hum_soil2, 'value': self.rpi.soil_hum_cap2()},
                                  {'variable': self.temp_soil, 'value': self.rpi.ds18b20.get_temperature()},
                                  ])

    def get_auto_state(self):
        """

        :return:
        """


# temp_rpi = api.get_variable('60a647851d8472029fed5c66')
# temp_soil = api.get_variable('60a648081d847205570d4f6a')
#
# temp_rpi.save_value({'value':rpi.aht10_temp()})
# temp_soil.save_value({'value':rpi.ds18b20.get_temperature()})





while True:
    collect_to_dashboard()
    time.sleep(60)
