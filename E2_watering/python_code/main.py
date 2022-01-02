"""
Script principal du projet
"""

# %% Importation des librairies
from classes import Button, Led, Arrosage, Measures  # Classes du projet
import time
from datetime import datetime, timedelta
import soil_cron
from dashboard import Dashboard

# %% Initialisation du programme
btn1 = Button(buttonPin=3, ledPin=2, ledInverted=True)
btn2 = Button(buttonPin=6, ledPin=5, ledInverted=True)

led = Led(4, inverted=True)
mes = Measures()
arrosage = Arrosage(relayPin=8, led=led, measureClass=mes, btn1=btn1, btn2=btn2)
dashboard = Dashboard()
last_dashboard_connection = datetime.now()
# %% Boucle infinie
arrosage.off()

arrosage.initMeasures()

last_btn1 = False
last_btn2 = False

while True:
    now = datetime.now()
    btn1_state = btn1.read_state()
    btn2_state = btn2.read_state()
    time.sleep(0.1)  # Attente pour ne pas surcharger le RPi
    # En mode arrosage automatique
    if arrosage.forced:
        arrosage.forced_loop()
        arrosage.btn2.led.on()
    else:
        arrosage.btn2.led.off()

    if arrosage.auto:
        arrosage.auto_loop()
        arrosage.btn1.led.on()
    else:
        arrosage.btn1.led.off()


    # Gestion des boutons de l'arrosage
    # Forçage de l'arrosage  (Bouton 2)
    if btn2_state and not last_btn2:
        print("Appui sur bouton 2")
        # Allumage de l'arrosage forcé
        if not arrosage.forced:
            arrosage.forced = True
            arrosage.on()
            arrosage.forced_start = now
        # Extinction de l'arrosage forcé
        else:
            arrosage.forced = False
            arrosage.off()


    # Activation de l'automatisation de l'arrosage (Bouton 1)
    if btn1_state and not last_btn1:
        print("Appui sur bouton 1")
        # Allumage de l'arrosage forcé
        if not arrosage.auto:
            arrosage.auto = True
            arrosage.off()
        # Extinction de l'arrosage forcé
        else:
            arrosage.off()
            arrosage.auto = False
    last_btn1 = btn1_state
    last_btn2 = btn2_state

    # Publication des mesures sur la dashboard
    if now - last_dashboard_connection > timedelta(minutes=3):
        last_dashboard_connection = now
        # Enregistrement des données dans report.csv
        soil_cron.save_to_csv("/home/pi/E2_watering/report/report.csv", arrosage.state)
        # Publication des mesures
        dashboard.publish_sensors()
        # Publication des états
        dashboard.set_arrosage_state(int(arrosage.state))
        dashboard.set_arrosage_forced(int(arrosage.forced))
        dashboard.set_auto_state(int(arrosage.auto))

