# Import the needed modules
import grove_rgb_lcd
import grovepi
import time
from grove_rgb_lcd import *
from w1thermsensor import W1ThermSensor, Unit



# Connect the Light Sensor to analog port A0
light_sensor = 0

# Connect the LEDs to digital port D4 & D3
led = 3
LED = 4

# Variables
sensor = W1ThermSensor()

# Analog port A0 set to INPUT
grovepi.pinMode(light_sensor,"INPUT")

# Digital port D4 & D3 set to OUTPUT
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(LED, "OUTPUT")

# Threshold to turn the led on
thresholdL = 400
thresholdT = 30

# Initial delay of 1 second
time.sleep(1)

while True: 
    try:
        # Read the light level
        light_value = grovepi.analogRead(light_sensor)
        print(light_value)
        # Read the Temp level
        temperature_in_C = sensor.get_temperature()
        print(temperature_in_C)

        # Display on the screen
        l = str(light_value)
        t = str(temperature_in_C)
        setText("Light_value=" + l + " Temp=" + t + "C")
        time.sleep(1)
        # Screen color
        grove_rgb_lcd.setRGB(244,0,0)


        if light_value < thresholdL:
            # Send LOW to switch on Led
            grovepi.digitalWrite(led,1)

        else:
            grovepi.digitalWrite(led,0)

        if temperature_in_C > thresholdT:
            # Set HIGH to switch off LED
            grovepi.digitalWrite(LED,0)
            time.sleep(1)
        else:
            grovepi.digitalWrite(LED,1)

    except KeyboardInterrupt as e:
        # Turn the LEDs off before stopping
        print(str(e))
        grovepi.digitalWrite(led,0)
        print(str(e))
        grovepi.digitalWrite(LED,1)
        break
    except IOError:
        print("error")

