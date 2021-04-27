from w1thermsensor import W1ThermSensor, Unit
import time
sensor1 = W1ThermSensor()

while True:
    temperature_in_all_units = sensor1.get_temperature()
    print(temperature_in_all_units)
    time.sleep(1)
