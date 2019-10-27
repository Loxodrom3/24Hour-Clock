# import busio
import adafruit_ds3231
import time
import board
# below are for oled
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

font = terminalio.FONT
displayio.release_displays()

i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
oled = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

rtc = adafruit_ds3231.DS3231(i2c)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# if False:   # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    # t = time.struct_time((2019,  10,   26,   22,  39,  15,    0,   -1,    -1))
    # rtc.datetime = t
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

# set up Text label
text_display = "Denver Time"
clock_group = displayio.Group()

while True:
    current = rtc.datetime

    # set time and labels for display to oled
    time_display = "{:d}:{:02d}:{:02d}".format(current.tm_hour, current.tm_min, current.tm_sec)

    text = label.Label(font, text=text_display)
    clock = label.Label(font, text=time_display)

    (_, _, width, _) = text.bounding_box
    text.x = 50
    text.y = 10
    clock = label.Label(font, text=time_display)
    
    (_, _, width, _) = clock.bounding_box
    clock.x = 60
    clock.y = 20
    
    clock_group = displayio.Group()
    clock_group.append(text)
    clock_group.append(clock)

    print(time_display)
    oled.show(clock_group)
    
    time.sleep(0.1)  
