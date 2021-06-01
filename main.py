# %% Importation des librairies
from classes import Button, Led, Arrosage, Measures  # Classes du projet
import time
# %% Initialisation du programme
btn1 = Button(buttonPin=3, ledPin=2, ledInverted=True)
btn2 = Button(buttonPin=6, ledPin=5, ledInverted=True)

led = Led(4, inverted=True)
mes = Measures()
arrosage = Arrosage(relayPin=8, led=led, measureClass=mes, btn1=btn1, btn2=btn2)

# %% Boucle infinie
arrosage.off()

while True:

    # En mode arrosage automatique
    if arrosage.auto:
        arrosage.auto_loop()


    # # Forçage de l'arrosage automatique (Bouton un)
    # if arrosage.is_btn_pressed(2):
    #     print("Button 2")
    #     # Allumage de l'arrosage forcé
    #     if not arrosage.forced:
    #         arrosage.forced = True
    #         arrosage.on()
    #
    #     # Exctinction de l'arrosage forcé
    #     else:
    #         arrosage.forced = False
    #         arrosage.off()
    # if btn1.read_state():
    #     print(1)
    # if btn2.read_state():
    #     print(2)
    #
    # # Arrosage
