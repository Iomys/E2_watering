## Importation des librairies
from classes import Button, Led, Wheather

##Initialisation du programme
btn1 = Button(buttonPin=2, ledPin=3, ledInverted=True)
btn2 = Button(buttonPin=6, ledPin=5, ledInverted=True)

led = Led(4, inverted=True)
## Boucle infinie

while True:
