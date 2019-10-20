# import busio
import adafruit_pcf8523
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

myI2C = board.I2C()  # busio.I2C(board.SCL, board.SDA)
rtc = adafruit_pcf8523.PCF8523(i2c)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if False:   # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2019,  10,   14,   11,  8,  45,    0,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

while True:
    current = rtc.datetime
    # print(t)     # uncomment for debugging
    print("The date is %s %d/%d/%d" % (days[current.tm_wday], current.tm_mon, current.tm_mday, current.tm_year))
    print("The time is %d:%02d:%02d" % (current.tm_hour, current.tm_min, current.tm_sec))

    # set time and labels for display to oled
    text_display = "Denver Time"
    time_display = "{:d}:{:02d}:{:02d}".format(current.tm_hour, current.tm_min, current.tm_sec)

    text  = label.Label(font, text=text_display)
    clock = label.Label(font, text=time_display)

    (_, _, width, _) = text.bounding_box
    text.x = 10
    text.y = 5

    (_, _, width, _) = clock.bounding_box
    clock.x = 10
    clock.y = 17
    
    clock_group = displayio.Group()
    clock_group.append(text)
    clock_group.append(clock)
    
    oled.show(clock_group)

    time.sleep(0.9)  
