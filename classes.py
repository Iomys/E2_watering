import time
import grovepi
import logging
from AHT10 import AHT10
from datetime import datetime, timedelta  # Gestion de date et heure
import csv
from w1thermsensor import W1ThermSensor

from pyowm import OWM  # OpenWheatherMap package
from pyowm.utils.config import get_config_from

class Led():
    """
    Leds du tableau de commande
    """
    state = False  #True pour allumée, False pour éteinte
    def __init__(self, pin, inverted=False):
        self.pin = pin
        self.inverted = inverted
        grovepi.pinMode(self.pin, "OUTPUT") #Initialisation du port
        self.off()  #La LED commence éteinte
    def on(self):
        """Allumer la LED"""
        if self.inverted:
            grovepi.digitalWrite(self.pin, 0)
        else:
            grovepi.digitalWrite(self.pin, 1)

        self.state = True

    def off(self):
        """Eteindre la LED"""
        if self.inverted:
            grovepi.digitalWrite(self.pin, 1)
        else:
            grovepi.digitalWrite(self.pin, 0)

        self.state = False

    def toggle(self):
        """Change l'état de la LED (de allumer à éteint ou inversément)"""
        if self.state: #Si la LED est allumée
            self.off()
        else:
            self.on()

class Button():
    """
    Bouton possédant une led sur le boitier de commande du raspberry pi
    """
    state = False
    def __init__(self, ledPin, buttonPin, ledInverted=True):
        self.led = Led(ledPin, ledInverted)
        self.pin = buttonPin
        #grovepi.set_pin_interrupt(self.pin)
        #grovepi.set_pin_interrupt(3, grovepi.COUNT_CHANGES, grovepi.FALLING, 100)
        grovepi.pinMode(self.pin, "INPUT")
    def read_state(self):
        state = grovepi.digitalRead(self.pin)
        if state:
            self.led.on()
        else:
            self.led.off()
        self.state = state
        print(state)
        return state
class Wheather():

    def __init__(self, api_key='029ee2f1a08c0add6d9ce67aa965f04c', lat=46.46790, long=6.86036):
        config_dict = get_config_from('wheather_api_config.json')
        owm = OWM(api_key, config_dict)
        self.mgr = owm.weather_manager()

        self.lat = lat
        self.long = long


    def rain(self):
        forecast = self.mgr.forecast_at_coords(self.lat, self.long, '3h').forecast

        rain_next_days = [0, 0, 0, 0, 0]  # Tableau contenant la quantité de pluie des 5 prochains jours

        # Compilation des prévisions jour par jour à la place de 3h par 3h
        for element in forecast:
            timeDiff = datetime.fromtimestamp(element.reference_time()) - datetime.now()
            if len(element.rain) != 0:  # S'il n'y a pas de pluie prévue le dictionnaire est vide (cas à exclure)
                rain_next_days[timeDiff.days] += element.rain['3h']
        return rain_next_days
    def rain_5_day(self):
        return sum(self.rain())
    def rain_next_day(self):
        return sum(self.rain()[0:1])


class Measures():
    dht_port = 4

    hum_chin_port = 0
    hum_cap1_port = 1
    hum_cap2_port = 2


    def __init__(self):
        try:
            self.ds18b20 = W1ThermSensor()  #Capteur de température 1Wire
            self.aht = AHT10(1)  #Capteur de température et d'humidité I2C
        except:
            pass

    def soil_hum_chin(self):
        try:
            return grovepi.analogRead(self.hum_chin_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité Chinois : \n {e}")

    def soil_hum_cap1(self):
        try:
            return grovepi.analogRead(self.hum_cap1_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité capacitif : \n {e}")

    def soil_hum_cap2(self):
        try:
            return grovepi.analogRead(self.hum_cap2_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité HES : \n {e}")

    def soil_temp(self):
        try:
            return self.ds18b20.get_temperature()
        except Exception as e:
            logging.error(f"Erreur avec le DS18B20 : \n {e}")

    def aht10_temp(self):
        try:
            return self.aht.getData()[0]
        except Exception as e:
            logging.error(f"Erreur dans la lecture de la température AHT10 : \n {e}")

    def aht10_hum(self):
        try:
            return self.aht.getData()[1]
        except Exception as e:
            logging.error(f"Erreur dans la lecture de l'humidité AHT10 : \n {e}")


