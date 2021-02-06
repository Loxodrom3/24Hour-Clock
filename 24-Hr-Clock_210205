# -----------------------
import time
import board
import displayio
import terminalio
import neopixel
import digitalio
import adafruit_ahtx0

from adafruit_display_text import label
import adafruit_displayio_sh1107

import adafruit_ds3231

# SetUp SunRise and SunSet for Feb and Mar
sunRise = 426, 425, 424, 423, 422, 421, 420, 419, 417, 416, 415, 414, 413, 411, 410, 409, 407, 406, 405, 403, 402, 401, 399, 398, 396, 395, 393, 392, 390, 389, 387, 386, 384, 383, 381, 380, 378, 377, 375, 373, 372, 430, 429, 427, 425, 424, 422, 421, 419, 417, 416, 414, 413, 411, 409, 408, 406, 405, 403
sunSet  = 1040, 1042, 1043, 1044, 1045, 1046, 1048, 1049, 1050, 1051, 1052, 1053, 1055, 1056, 1057, 1058, 1059, 1060, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 

displayio.release_displays()

# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# Create the sensor object using I2C
sensor = adafruit_ahtx0.AHTx0(board.I2C())

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

# Text set up for Time, Temp, and Humidity
text0 = ("MST:   " )
text1 = ("Temp: %0.1f C" % sensor.temperature)  # overly long to see where it clips
text2 = ("Hum:  %0.1f %%" % sensor.relative_humidity)
text_Time = label.Label(terminalio.FONT, text=text0, color=0xFFFFFF, x=8, y=12)
text_TempC= label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=8, y=30)
text_Temp = label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=90, y=30)
text_Hum = label.Label(terminalio.FONT, text=text2, color=0xFFFFFF, x=8, y=48)
splash.append(text_Time)
splash.append(text_Temp)
splash.append(text_TempC)
splash.append(text_Hum)

# -------------------------------------
# SetUp HeartBeat
ledHB = digitalio.DigitalInOut(board.D13)
ledHB.direction = digitalio.Direction.OUTPUT
ledHB.value = True

# SetUp NeoPixels
LEDPin = board.A1
numLED = 60
ORDER = neopixel.GRBW
ringLED = neopixel.NeoPixel(LEDPin, numLED, brightness=0.5, auto_write=False, pixel_order=ORDER)

rtc = adafruit_ds3231.DS3231(i2c)

# RGBW values for the Background, Now, Day and Night.
nowRed = 10
nowGrn = 0
nowBlu = 20
nowWht = 0

dayRed = 22
dayGrn = 10
dayBlu = 0
dayWht = 0

nitRed = 0
nitGrn = 10
nitBlu = 50
nitWht = 0

prsRed = 0
prsGrn = 0
prsBlu = 0
prsWht = 25

monthDay = 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334  # since RTC are not supporting dayOfYear, I am using this for calculating the number of days pass by the month.  And this is using 28 days in Feb.  NOT a Leap Year...
# monthDay = 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335  # use this array for leap years
toDay = 0
currMin = 0
currSec = 0
decSec = 0
sleepTime = 0.086

#if False:   # change to True if you want to write the time!
    #                       year, mon, date, hour, min, sec, wday, yday, isdst
    # t = time.struct_time((2021,  02,   05,   18,  23,  30,    0,   -1,    -1))
    #  rtc.datetime = t
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

for i in range(0, numLED, 1):
    ringLED[i] = (nitRed, nitGrn, nitBlu, nitWht)
ringLED.show()

while True:
    current = rtc.datetime
    hurOfDay = (((current.tm_hour)%24))
    minOfDay = (((current.tm_hour)%24)*60) + current.tm_min
    secOfDay = ((((current.tm_hour)%24)*60*60) + (current.tm_min*60)) + current.tm_sec
    dayOfYear = monthDay[current.tm_mon - 1] + current.tm_mday  # using '- 1' because Jan is month 1, and index for monthDay starts at 0

    if toDay != dayOfYear:  # Calculate the setPixel and risePixel when its a new day
        toDay = dayOfYear
        risePixel = int((numLED*(sunRise[toDay-(monthDay[current.tm_mon - 1])])/1440)+ (numLED/2) )
        risePct = ((numLED*(sunRise[toDay])/1440) + (numLED / 2)) - 1 - risePixel
        setPixel  = int((numLED*(sunSet[toDay]) /1440) -(numLED/2) ) 
        setPct = ((numLED*(sunSet[toDay])/1440) - (numLED / 2)) - setPixel

    if currMin != minOfDay:
        currMin = minOfDay
        nowPixel = int(((numLED/2) + (numLED*(secOfDay/86400)))%numLED ) # 86400 seconds in a day
        # set pixels for ring and now
        for i in range(0, setPixel, 1):
            ringLED[i] = (dayRed, dayGrn, dayBlu, dayWht)
        for i in range(setPixel, risePixel, 1):
            ringLED[i] = (nitRed, nitGrn, nitBlu, nitWht)
        for i in range(risePixel, numLED, 1):
            ringLED[i] = (dayRed, dayGrn, dayBlu, dayWht)
        ringLED[nowPixel] = (nowRed, nowGrn, nowBlu, nowWht)
        ringLED.show()

    time_display = "{:d}:{:02d}:{:02d}".format(current.tm_hour, current.tm_min, current.tm_sec)
    text_Time.text = (time_display)
    text_Time.x=42
    text_TempC.text = ("Temp: %0.1f C" % sensor.temperature)
    text_TempC.x=8
    text_Temp.text = ("%0.1f F" % (sensor.temperature*9/5+32))
    text_Hum.text = ("Hum:  %0.1f %%" % sensor.relative_humidity)
    text_Hum.x=8
    # display.show(splash)

    print(time_display)
    print("Temp: %0.1f C" % sensor.temperature)
    print("Hum:  %0.1f %%" % sensor.relative_humidity)
    print("\n")

    ledHB.value = not ledHB.value
    time.sleep(0.5)
