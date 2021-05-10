from datetime import datetime
import csv
from main import Measures
mes = Measures()

with open('/home/pi/E2_watering/report/soil_moisture.csv', 'a', newline='') as csvfile:

    output = [datetime.now().isoformat(), mes.soil_hum_chin(), mes.soil_hum_hes(), mes.soil_hum_cap()]
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(output)
    print(output)
