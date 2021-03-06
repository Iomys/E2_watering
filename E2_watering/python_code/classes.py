
import grovepi
import logging
import numpy as np
from AHT10 import AHT10
from datetime import datetime, timedelta, time  # Gestion de date et heure
from w1thermsensor import W1ThermSensor

from pyowm import OWM  # OpenWheatherMap package
from pyowm.utils.config import get_config_from

class Led:
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

class Button:
    """
    Bouton possédant une led sur le boitier de commande du raspberry pi
    """
    state = False
    def __init__(self, ledPin, buttonPin, ledInverted=True):
        self.led = Led(ledPin, ledInverted)
        self.pin = buttonPin

        grovepi.pinMode(self.pin, "INPUT")
    def read_state(self):
        state = grovepi.digitalRead(self.pin)
        # if state:
        #     self.led.on()
        # else:
        #     self.led.off()
        self.state = state
        return state
    
class Wheather:

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
        return sum(self.rain()[0:2])


class Measures:
    dht_port = 4

    hum_chin_port = 0
    hum_cap1_port = 1
    hum_cap2_port = 2
    hum_cap0_port = 0

    hum_max = 280  # 100% d'humidité
    hum_min = 500  # 0% humidité


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
            logging.error(f"Erreur avec Capteur d'humidité capacitif 1: \n {e}")

    def soil_hum_cap2(self):
        try:
            return grovepi.analogRead(self.hum_cap2_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité capacitif 2 : \n {e}")

    def soil_hum_cap0(self):
        try:
            return grovepi.analogRead(self.hum_cap0_port)
        except (IOError, TypeError) as e:
            logging.error(f"Erreur avec Capteur d'humidité capacitif 3 : \n {e}")

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

    def humidity_to_percent(self, humidity):
        """
        Fonction convertissant la valeur analogique de l'humidité du sol en pourcentage d'humidité.
        :param humidity: valeur analogique de l'humidité
        :return: pourcentage d'humidité du sol.
        """
        if self.hum_min > self.hum_max:
            # Cas ou plus il y a d'humidité, moins le capteur affiche une valeur grande.
            humidity = humidity - self.hum_max
            percents = 1 - humidity/(self.hum_min - self.hum_max)
        else:
            humidity = humidity - self.hum_min
            percents = humidity / (self.hum_max - self.hum_min)
        return percents


class Arrosage:
    state = False
    auto = True
    forced = False

    # Définition des seuils d'humidité
    hum_to_water = 0.8
    hum_cible = 2/3
    hum_critical = 1/4


    rain_max = 10 # Seuil de pluie prévue pour annuler l'arrosage
    forced_start = datetime(2021, 1, 1)

    humidity = None
    # Initialisation d'un tableau pour sauvegarder les mesures.
    mean_size = 20
    historic_hum = np.zeros(mean_size)
    historic_hum[:] = np.nan
    last_loop = datetime(2021, 1, 1)  # Au démarrage la boucle sera directement activée

    def __init__(self, relayPin: int, led: Led, measureClass: Measures, btn1: Button, btn2: Button):
        """

        :param relayPin: pin d'entrée pour le relais contrôlant l'arrosage automatique.
        :param led: Classe de la Led qui s'allume quand l'arrosage est en fonction (LED2 sur le schéma)
        :param measureClass: classe de mesure du projet
        """
        # Passage des paramètres

        self.btn1 = btn1
        self.btn2 = btn2
        self.led = led
        self.measureClass = measureClass
        self.relayPin = relayPin

        # Initialisations diverses
        self.wheather = Wheather()
        grovepi.pinMode(self.relayPin, "OUTPUT")

        self.off()  # L'arrosage commence éteint

    def on(self):
        """Allumer le relais (donc l'arrosage)"""
        grovepi.digitalWrite(self.relayPin, 1)
        self.led.on()
        self.state = True

    def off(self):
        """Eteindre le relais (donc l'arrosage)"""
        self.led.off()
        grovepi.digitalWrite(self.relayPin, 0)
        self.state = False

    def get_humidity(self):
        """
        Mesure de l'humidité, vérification de la validité de cette mesure.
        Retourne la moyenne des 50 dernières mesures.

        :return: string : "critical", "low" or "good"
        """
        mesure = self.measureClass.soil_hum_cap2()

        # Supression valeur trop grande
        while mesure > 1024:
            mesure = self.measureClass.soil_hum_cap2()
        self.historic_hum = np.roll(self.historic_hum, 1)  # Décalage du tableau vers la droite
        self.historic_hum[0] = mesure  # On ajoute la dernière mesure
        # Détection d'une possible valeur erronée isolée
        gapMax = 20
        if abs(self.historic_hum[1] - (self.historic_hum[0]+self.historic_hum[2])/2) > gapMax:
            # On remplace la valeur erronée par la moyenne des deux valeurs autour
            self.historic_hum[1] = self.historic_hum[2]

        # Moyenne des dernières valeurs de l'humidité pour "lisser la courbe"
        humidity = np.mean(self.historic_hum[1:])
        self.humidity = humidity
        return humidity

    def is_btn_pressed(self, num):
        """
        :param num: Indice du bouton à observer
        :return: Retourne True lorsque le bouton choisi est appuyé
        """
        if num == 1:
            # Détection de l'appui sur le bouton 1 (seulement état montant)
            if self.btn1.state == False and self.btn1.read_state() == True:
                output = True
            else:
                output = False
            self.btn1.read_state()
        elif num == 2:
            # Détection de l'appui sur le bouton 2 (seulement état montant)
            if self.btn2.state == False and self.btn2.read_state() == True:
                output = True
            else:
                output = False

            self.btn1.read_state()
        else:
            raise

        return output

    def activate(self):
        self.auto = True

    def deactivate(self):
        self.auto = False
        self.off()

    def auto_loop(self):
        # La boucle est activée une seule fois toutes les deux minutes.
        if datetime.now() - self.last_loop > timedelta(minutes=2):
            self.last_loop = datetime.now()
            # On lis la valeur du capteur d'humidité convertie en pourcents
            hum = self.measureClass.humidity_to_percent(self.get_humidity())
            print(datetime.now(), ":", hum, ", ", self.measureClass.soil_hum_cap2(), self.measureClass.humidity_to_percent(self.measureClass.soil_hum_cap2()))
            # Si l'humidité est plus grande que le seuil d'arret voulu pour l'arrosage
            if hum > self.hum_to_water:
                self.off()
                print("Humidité au max, arrosage éteint")
            # Si l'humidité est faible et qu'il ne pleut pas le lendemain et que c'est la nuit
            elif hum < self.hum_cible and self.wheather.rain_next_day() < self.rain_max and \
                    time(18, 00) < datetime.now().time() or datetime.now().time() < time(8, 00):
                self.on()
                print("Allumage de l'arrosage : pas de pluie prévue")
            # Si l'muhidité est critique, on arrosage meme s'il annonce de la pluie le lendemain
            elif hum < self.hum_critical:
                print("Allumage de l'arrosage : sol très sec !")
                self.on()

    def initMeasures(self):
        """
        A l'initialisation du programme, on prend directement le même nombre de mesures que le nombre sur lequel on
        effectue la moyenne flotante, afin d'avoir un nombre dès la première mesure et non nan.
        :return: Nothing
        """
        for i in range(self.mean_size):
            print(self.get_humidity())

    def forced_loop(self):
        if datetime.now() - self.last_loop > timedelta(minutes=1):
            self.last_loop = datetime.now()
            # On lit la valeur du capteur d'humidité convertie en pourcents
            hum = self.measureClass.humidity_to_percent(self.get_humidity())
            if hum > self.hum_to_water:
                self.off()
                self.forced = False
                print("Humidité au max, arrosage éteint")

        if datetime.now() - self.forced_start > timedelta(minutes=45):
            self.off()
            self.forced = False
            print("Arrosage pendant 45 min, extinction")




