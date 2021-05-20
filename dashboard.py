import time

from ubidots import ApiClient
from classes import Measures

API_TOKEN = "BBFF-lyOOKy3EBYeAzaruUbMk0E8mckUCQ9"
rpi = Measures()

dashboard = ApiClient(token=API_TOKEN)
temp_rpi = '60a647851d8472029fed5c66'
temp_soil = '60a648081d847205570d4f6a'
hum_rpi = '60a648061d84720586158528'
hum_soil0 = '60a648091d847205b05a2494'
hum_soil1 ='60a6480a1d847205e954744f'
hum_soil2 = '60a6480c1d847205e9547450'
def collect_to_dashboard():
    dashboard.save_collection([{'variable': temp_rpi, 'value': rpi.aht10_temp()},
                     {'variable': hum_rpi, 'value':rpi.aht10_hum()},
                     {'variable': hum_soil0, 'value': rpi.soil_hum_chin()},
                     {'variable': hum_soil1, 'value': rpi.soil_hum_cap1()},
                     {'variable': hum_soil2, 'value': rpi.soil_hum_cap2()},
                     {'variable': temp_soil, 'value': rpi.ds18b20.get_temperature()},
                     ])


# temp_rpi = dashboard.get_variable('60a647851d8472029fed5c66')
# temp_soil = dashboard.get_variable('60a648081d847205570d4f6a')
#
# temp_rpi.save_value({'value':rpi.aht10_temp()})
# temp_soil.save_value({'value':rpi.ds18b20.get_temperature()})





while True:
    collect_to_dashboard()
    time.sleep(60)
