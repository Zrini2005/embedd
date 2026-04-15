# | Segment | GPIO Pin          |
# | ------- | ----------------- |
# | a       | GPIO 17           |
# | b       | GPIO 18           |
# | c       | GPIO 27           |
# | d       | GPIO 22           |
# | e       | GPIO 23           |
# | f       | GPIO 24           |
# | g       | GPIO 25           |
# | dp      | GPIO 4 (optional) |

# 7 Segment Display with Raspberry Pi

import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)

segments = [17, 18, 27, 22, 23, 24, 25]  # a,b,c,d,e,f,g

for pin in segments:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# Digit patterns (a,b,c,d,e,f,g)
digits = {
    0: [1,1,1,1,1,1,0],
    1: [0,1,1,0,0,0,0],
    2: [1,1,0,1,1,0,1],
    3: [1,1,1,1,0,0,1],
    4: [0,1,1,0,0,1,1],
    5: [1,0,1,1,0,1,1],
    6: [1,0,1,1,1,1,1],
    7: [1,1,1,0,0,0,0],
    8: [1,1,1,1,1,1,1],
    9: [1,1,1,1,0,1,1]
}

def display(num):
    for i in range(7):
        GPIO.output(segments[i], digits[num][i])

try:
    while True:
        for i in range(10):
            display(i)
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
