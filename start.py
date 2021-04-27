# Import the needed modules
import grovepi
import time

# Connect the LED to digital port D4
LED = 4

# Digital port D4 set to OUTPUT
grovepi.pinMode(led,"OUTPUT")

# Initial delay of 1 second
time.sleep(1)

while True:
    try:
        # Blink the LED
        # Send HIGH to switch on LED
        grovepi.digitalWrite(led,1)
        time.sleep(1)
        # Send LOW to switch off LED
        grovepi.digitalWrite(led,0)
        time.sleep(1)
    except KeyboardInterrupt as e:
        # Turn the LED off before stopping
        print(str(e))
        grovepi.digitalWrite(led,0)
        break
    except (IOError, TypeError) as e:
        # Turn the LED off before stopping
        print(str(e))
        grovepi.digitalWrite(led,0)

