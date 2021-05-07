from w1thermsensor import W1ThermSensor, Unit
import time
sensor1 = W1ThermSensor()

while True:
    temperature_in_C = sensor1.get_temperature()
    print(temperature_in_C)
    time.sleep(1)
    #Petit commentaire
