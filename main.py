import time
import grovepi
import logging
from datetime import datetime
import csv

class Measures():
    dht_port = 4
    hum_cap_port = 0
    hum_chin_port = 2
    hum_hes_port = 1

    def dht_temp(self):
        try:
            [temp, hum] = grovepi.dht(self.dht_port, 0)
            return temp
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec dht11 : \n {e}")

    def dht_hum(self):
        try:
            [temp, hum] = grovepi.dht(self.dht_port, 0)
            return hum
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec dht11 : \n {e}")

    def soil_hum_chin(self):
        try:
            return grovepi.analogRead(self.hum_chin_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité Chinois : \n {e}")

    def soil_hum_cap(self):
        try:
            return grovepi.analogRead(self.hum_cap_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité capacitif : \n {e}")

    def soil_hum_hes(self):
        try:
            return grovepi.analogRead(self.hum_hes_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité HES : \n {e}")

    # def soil_temp(self):


# mes = Measures()
# print("HES \tChinois \tCapacitif")
# while True:
#     with open('/home/pi/E2_watering/report/soil_moisture.csv', 'a', newline='') as csvfile:
#         output = [datetime.now().isoformat(), mes.soil_hum_chin(), mes.soil_hum_hes(), mes.soil_hum_cap()]
#         writer = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(output)
#     print(output)
#     time.sleep(1*60*5)

# mes = Measures()

# with open('/home/pi/E2_watering/report/soil_moisture.csv', 'a', newline='') as csvfile:
#     print("1")
#
#     output = [datetime.now().isoformat(), mes.soil_hum_chin(), mes.soil_hum_hes(), mes.soil_hum_cap()]
#     print('2')
#     writer = csv.writer(csvfile, delimiter=',',
#                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     print('3')
#     writer.writerow(output)
#     print(output)
