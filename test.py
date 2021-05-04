import grovepi
import time

Soil_sensor = 2

grovepi.pinMode(Soil_sensor,"INPUT")

while True:
    try:
        humidity_level = grovepi.analogRead(Soil_sensor)
        print(humidity_level)
        time.sleep(1)
    except KeyboardInterrupt:
        print("end")
        break