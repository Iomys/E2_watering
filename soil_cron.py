from datetime import datetime
import csv
from classes import Measures
mes = Measures()
print("Iinit")
with open('/home/pi/E2_watering/report/soil_moisture.csv', 'a', newline='') as csvfile:

    output = [datetime.now().isoformat(), mes.soil_hum_chin(), mes.soil_hum_cap1(), mes.soil_hum_cap2(), mes.ds18b20.get_temperature(), mes.aht10_temp(), mes.aht10_hum()]
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(output)
    print(output)
