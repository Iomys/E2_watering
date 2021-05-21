    # Importation des divers packages
from pyowm import OWM  # OpenWheatherMap package
from pyowm.utils.config import get_config_from
from datetime import datetime, timedelta  # Gestion de date et heure
import grovepi
import time

led = 2
threshold = 1

grovepi.pinMode(led,"output")

# Initilaisation de l'API de OpenWheatherMap
lat, long = 46.46790, 6.86036  # Localisation de la Maison
config_dict = get_config_from('wheather_api_config.json')
owm = OWM('029ee2f1a08c0add6d9ce67aa965f04c', config_dict)
mgr = owm.weather_manager()

# Obtention des prévisions 3h par 3h pour les 5 prochains jours
forecast = mgr.forecast_at_coords(lat, long, '3h').forecast

rain_next_days = [0, 0, 0, 0, 0]  # Tableau contenant la quantité de pluie des 5 prochains j
# Compilation des prévisions jour par jour à la place de 3h par 3h
for element in forecast:
    timeDiff = datetime.fromtimestamp(element.reference_time())-datetime.now()
    if len(element.rain) != 0:  # S'il n'y a pas de pluie prévue le dictionnaire est vide (cas à exclure)
        rain_next_days[timeDiff.days] += element.rain['3h']

# Affichage les  prévisions de pluie
print(f"""Voici la quantité de pluie prévue ces prochains jours : """)
for i in range(0, 5):
    print((datetime.now() + timedelta(days=i)).strftime('%A'), ":", rain_next_days[i], "mm de pluie")

if rain_next_days[0] > threshold:
    grovepi.digitalWrite(led,1)
    time.sleep(3)
    grovepi.digitalWrite(led,0)