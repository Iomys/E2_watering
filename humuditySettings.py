import grovepi
import time
from datetime import datetime, timedelta
from classes import Measures
import csv
soil_sensor = 2
vanne = 3
mes = Measures()
grovepi.pinMode(soil_sensor,"INPUT")
grovepi.pinMode(vanne,"OUTPUT")
lastMeasure = datetime.now()
while True:
    if (datetime.now()-lastMeasure).total_seconds() >= 1*60*10:
        lastMeasure = datetime.now()

        with open('/home/pi/E2_watering/report/soil_moisture.csv', 'a', newline='') as csvfile:

            output = [datetime.now().isoformat(), mes.soil_hum_chin(), mes.soil_hum_cap1(), mes.soil_hum_cap2(),
                      mes.ds18b20.get_temperature(), mes.aht10_temp(), mes.aht10_hum()]
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(output)
            print(output)

        humidity = grovepi.analogueRead(soil_sensor)
        if humidity <= 680:
            grovepi.digitalWrite(vanne,1)
        else:
            grovepi.digitalWrite(vanne,0)






