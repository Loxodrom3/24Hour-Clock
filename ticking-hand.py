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

base = 100

for i in range(0, numLED, 1):
    ringLED[i] = (35, 0, 9)

ringLED.show()

while True:
    
    for i in range(0, 100, 1):
        mark = (i/base)
        mark24 = int(mark * 24)
        mark12 = int(mark * 12)
        ringLED[mark24] = (35, 0, 150)
        ringLED[mark24-1] = (35, 0, 9)
        ringLED[mark12 + 24] = (35, 0, 150)
        ringLED[mark12 + 24 -1] = (35, 0, 9)
        ringLED.show()
        print(i, mark, mark24, sep=",  ")
        ledHB.value = not ledHB.value
        time.sleep(0.33)
