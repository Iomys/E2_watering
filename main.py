import time
import grovepi
import logging

class Measures():
    dht_port = 4
    hum_cap_port = 0
    hum_chin_port = 1
    hum_hes_port = 2

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
        try :
            return grovepi.analogRead(self.hum_chin_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité Chinois : \n {e}")
    def soil_hum_cap(self):
        try :
            return grovepi.analogRead(self.hum_cap_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité capacitif : \n {e}")
    def soil_hum_hes(self):
        try :
            return grovepi.analogRead(self.hum_hes_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité HES : \n {e}")

mes = Measures()
while True:
    print(grovepi.dht(4, 0))
    print(mes.dht_hum())
    time.sleep(1)


