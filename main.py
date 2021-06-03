# %% Importation des librairies
from classes import Button, Led, Arrosage, Measures  # Classes du projet
import time
from datetime import datetime
from dashboard import Dashboard

# %% Initialisation du programme
btn1 = Button(buttonPin=3, ledPin=2, ledInverted=True)
btn2 = Button(buttonPin=6, ledPin=5, ledInverted=True)

led = Led(4, inverted=True)
mes = Measures()
arrosage = Arrosage(relayPin=8, led=led, measureClass=mes, btn1=btn1, btn2=btn2)
dashboard = Dashboard()

# %% Boucle infinie
arrosage.off()

arrosage.initMeasures()

while True:

    time.sleep(0.1)  # Attente pour ne pas surcharger le RPi
    # En mode arrosage automatique
    if arrosage.forced:
        arrosage.forced_loop()

    elif arrosage.auto:
        arrosage.auto_loop()

    # Récupération des infos de la dashboard


    # Gestion des boutons de l'arrosage
    # Forçage de l'arrosage  (Bouton 2)
    if arrosage.is_btn_pressed(2):
        print("Appui sur bouton 2")
        # Allumage de l'arrosage forcé
        if not arrosage.forced:

            arrosage.forced = True
            arrosage.forced_start = datetime.now()
        # Extinction de l'arrosage forcé
        else:
            arrosage.forced = False

    # Activation de l'automatisation de l'arrosage (Bouton 1)
    if arrosage.is_btn_pressed(1):
        print("Appui sur bouton 1")
        # Allumage de l'arrosage forcé
        if not arrosage.auto:

            arrosage.auto = True
        # Extinction de l'arrosage forcé
        else:
            arrosage.auto = False
