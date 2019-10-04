import time
import board
import simpleio
import neopixel
import digitalio
import math

# SetUp HeartBeat
ledHB = digitalio.DigitalInOut(board.D13)
ledHB.direction = digitalio.Direction.OUTPUT
ledHB.value = True

# SetUp NeoPixels
LEDPin = board.A1
numLED = 36
ORDER = neopixel.GRB
ringLED = neopixel.NeoPixel(LEDPin, numLED, brightness=0.2, auto_write=False, pixel_order=ORDER)

base = 200

for i in range(0, numLED, 1):
    ringLED[i] = (35, 0, 10)

ringLED.show()

while True:
    
    for i in range(0, base, 1):
        mark = i/base
        mark24 = int(mark * 24)
        pct24 = (mark * 24) - mark24
        mark12 = int(mark * 12)
        pct12 = (mark * 12) - mark12
        ra24 = int(10+(pct24*140))
        rb24 = int(200 - (10+(pct24*190)))
        ra12 = int(10+(pct12*140))
        rb12 = int(200 - (10+(pct12*190)))
        for i in range(0, numLED, 1):
            ringLED[i] = (35, 0, 10)
        ringLED[mark24] = (35, 0, ra24)
        ringLED[mark12 + 24] = (35, 0, ra12)
        ringLED[mark24 -1] = (35, 0, rb24)  # fade the trailing dot (s)
        ringLED[mark12 -1 + 24] = (35, 0, rb12)
        ringLED.show()
        print(i, mark, mark24, mark12, pct24, pct12, sep=",  ")
        ledHB.value = not ledHB.value
        time.sleep(0.1)
