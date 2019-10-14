# displays time, but then errors out.
import busio
import adafruit_pcf8523
import time
import board
# below are for oled
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)
# **********************

myI2C = board.I2C()  # busio.I2C(board.SCL, board.SDA)
rtc = adafruit_pcf8523.PCF8523(myI2C)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if False:   # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2019,  10,   14,   11,  8,  45,    0,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

    print("Setting time to:", t)     # uncomment for debugging
    rtc.datetime = t
    print()

while True:
    t = rtc.datetime
    # print(t)     # uncomment for debugging
    print("The date is %s %d/%d/%d" % (days[t.tm_wday], t.tm_mon, t.tm_mday, t.tm_year))
    print("The time is %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec))
    

    text = ""
    text = ("Time: %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec))
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
    splash.append(text_area)

    time.sleep(0.5)  # wait a second
