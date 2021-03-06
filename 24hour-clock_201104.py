import time
import board
import busio
import simpleio
import neopixel
import digitalio
import math
# for DS3231 Precision RTC and OLED
import adafruit_ds3231
import adafruit_bus_device
import adafruit_register
import displayio
# import terminalio
import adafruit_displayio_ssd1306
import busio
# from adafruit_display_text import label

# SetUp SunRise and SunSet
sunRise =  441, 441, 441, 441, 441, 441, 440, 440, 440, 440, 440, 439, 439, 439, 438, 438, 437, 437, 436, 436, 435, 434, 434, 433, 432, 432, 431, 430, 429, 428, 427, 426, 425, 424, 423, 422, 421, 420, 419, 418, 417, 416, 414, 413, 412, 411, 409, 408, 407, 405, 404, 403, 401, 400, 398, 397, 396, 394, 393, 391, 390, 388, 387, 385, 384, 382, 380, 379, 437, 436, 434, 433, 431, 429, 428, 426, 425, 423, 421, 420, 418, 417, 415, 413, 412, 410, 409, 407, 405, 404, 402, 401, 399, 397, 396, 394, 393, 391, 390, 388, 387, 385, 384, 382, 381, 379, 378, 376, 375, 373, 372, 371, 369, 368, 366, 365, 364, 363, 361, 360, 359, 358, 356, 355, 354, 353, 352, 351, 350, 349, 348, 347, 346, 345, 344, 343, 342, 341, 341, 340, 339, 338, 338, 337, 336, 336, 335, 335, 334, 334, 333, 333, 333, 332, 332, 332, 332, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 332, 332, 332, 332, 333, 333, 333, 334, 334, 335, 335, 336, 336, 337, 337, 338, 338, 339, 340, 340, 341, 342, 342, 343, 344, 345, 345, 346, 347, 348, 349, 349, 350, 351, 352, 353, 354, 355, 356, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 413, 414, 415, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 446, 447, 448, 449, 450, 391, 392, 393, 395, 396, 397, 398, 399, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 428, 429, 430, 431, 432, 432, 433, 434, 434, 435, 436, 436, 437, 437, 438, 438, 439, 439, 439, 440, 440, 440, 440, 440, 440
sunSet = 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1033, 1034, 1035, 1036, 1037, 1039, 1040, 1041, 1042, 1043, 1045, 1046, 1047, 1048, 1049, 1050, 1052, 1053, 1054, 1055, 1056, 1057, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1079, 1080, 1081, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1216, 1217, 1218, 1219, 1220, 1220, 1221, 1222, 1222, 1223, 1224, 1224, 1225, 1226, 1226, 1227, 1227, 1228, 1228, 1229, 1229, 1229, 1230, 1230, 1230, 1231, 1231, 1231, 1231, 1231, 1231, 1232, 1232, 1232, 1232, 1232, 1231, 1231, 1231, 1231, 1231, 1231, 1230, 1230, 1230, 1229, 1229, 1228, 1228, 1227, 1227, 1226, 1226, 1225, 1225, 1224, 1223, 1222, 1222, 1221, 1220, 1219, 1218, 1217, 1216, 1215, 1214, 1213, 1212, 1211, 1210, 1209, 1208, 1207, 1205, 1204, 1203, 1202, 1201, 1199, 1198, 1197, 1195, 1194, 1193, 1191, 1190, 1188, 1187, 1185, 1184, 1182, 1181, 1179, 1178, 1176, 1175, 1173, 1172, 1170, 1169, 1167, 1165, 1164, 1162, 1161, 1159, 1157, 1156, 1154, 1152, 1151, 1149, 1148, 1146, 1144, 1143, 1141, 1139, 1138, 1136, 1134, 1133, 1131, 1129, 1128, 1126, 1125, 1123, 1120, 1118, 1117, 1115, 1113, 1112, 1110, 1109, 1107, 1106, 1104, 1103, 1101, 1100, 1098, 1097, 1095, 1094, 1092, 1091, 1090, 1088, 1087, 1086, 1084, 1083, 1082, 1081, 1079, 1078, 1077, 1076, 1015, 1014, 1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004, 1003, 1003, 1002, 1001, 1001, 1000, 999, 999, 998, 998, 997, 997, 997, 996, 996, 996, 995, 995, 995, 995, 995, 995, 995, 995, 995, 995, 995, 995, 996, 996, 996, 996, 997, 997, 998, 998, 999, 999, 1000, 1000, 1001, 1002, 1002, 1003, 1004, 1004, 1005, 1005

# monthDay = 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334  # since RTC are not supporting dayOfYear, I am using this for calculating the number of days pass by the month.  And this is using 28 days in Feb.  NOT a Leap Year...
monthDay = 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335  # use this array for leap years
toDay = 0
currMin = 0
currSec = 0
decSec = 0
sleepTime = 0.073

base = 86400  # seconds in a day

# font = terminalio.FONT
# displayio.release_displays()

i2c = board.I2C()

# display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
# display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
# display_bus = displayio.I2CDisplay(i2c, device_address=0x3c, reset=board.D9)

# SetUp HeartBeat
ledHB = digitalio.DigitalInOut(board.D13)
ledHB.direction = digitalio.Direction.OUTPUT
ledHB.value = True

# SetUp NeoPixels
LEDPin = board.A1
numLED = 60
ORDER = neopixel.GRBW

ringLED = neopixel.NeoPixel(LEDPin, numLED, brightness=0.4, auto_write=False, pixel_order=ORDER)

rtc = adafruit_ds3231.DS3231(i2c)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Set clock on RTC.  Only need to do if RT  drifts, or the after changing battery in RTC
if False:   # change to True if you want to write the time!
    #                       year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2020,  11,  12,   23,  23,  20,    0,   -1,    -1))
    rtc.datetime = t
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

# RGBW values for the Background, Hour, Minute and Second.
bkgRed = 12
bkgGrn = 0
bkgBlu = 30
bkgWht = 0

hurRed = 0
hurGrn = 0
hurBlu = 0
hurWht = 0

minRed = 0
minGrn = 0
minBlu = 0
minWht = 0

secRed = 20
secGrn = 0
secBlu = 0
secWht = 0

nowRed = 30
nowGrn = 0
nowBlu = 0
nowWht = 0

dayRed = 8
dayGrn = 5
dayBlu = 0
dayWht = 7

nitRed = 8
nitGrn = 0
nitBlu = 40
nitWht = 0


for i in range(0, numLED, 1):
    ringLED[i] = (bkgRed, bkgGrn, bkgBlu, bkgWht)
ringLED.show()

while True:
    current = rtc.datetime
    hurOfDay = (((current.tm_hour)%24))
    minOfDay = (((current.tm_hour)%24)*60) + current.tm_min
    secOfDay = ((((current.tm_hour)%24)*60*60) + (current.tm_min*60)) + current.tm_sec
    dayOfYear = monthDay[current.tm_mon - 1] + current.tm_mday  # using '- 1' because Jan is month 1, and index for monthDay starts at 0

    if toDay != dayOfYear:  # Calculate the setPixel and risePixel when its a new day
        toDay = dayOfYear
        risePixel = int((numLED*(sunRise[toDay])/1440) )# + (numLED / 2)) - 1  # should use ceiling
        risePct = ((numLED*(sunRise[toDay])/1440) + (numLED / 2)) - 1 - risePixel
        setPixel  = int((numLED*(sunSet[toDay]) /1440)) # - (numLED / 2))  # 1440 is minutes in a day
        setPct = ((numLED*(sunSet[toDay])/1440) - (numLED / 2)) - setPixel

    #  Only calculate nowPixel and re-draw when minute increments
    if currMin != minOfDay:
        currMin = minOfDay
        nowPixel = int(numLED*(secOfDay/86400)) # 86400 seconds in a day
        # set pixels for ring and now
        for i in range(0, risePixel, 1):
            ringLED[i] = (nitRed, nitGrn, nitBlu, nitWht)
        for i in range(risePixel, setPixel, 1):
            ringLED[i] = (dayRed, dayGrn, dayBlu, dayWht)
        for i in range(setPixel, numLED, 1):
            ringLED[i] = (nitRed, nitGrn, nitBlu, nitWht)
        ringLED[nowPixel] = (nowRed, nowGrn, nowBlu, nowWht)
        ringLED.show()

    if currSec != current.tm_sec:
        currSec = current.tm_sec
        decSec  = 0

    time_display = "{:d}:{:02d}:{:02d}.{:03d}".format(current.tm_hour, current.tm_min, current.tm_sec, int(decSec*1000)) 
    print(time_display, sunRise[toDay], currMin, sunSet[toDay]) #, nowPixel)
    decSec = decSec + sleepTime

    # print(current.tm_hour, current.tm_min, current.tm_sec, risePixel, setPixel, nowPixel)
    # print(dayOfYear, hurOfDay, minOfDay, secOfDay, risePixel, setPixel, nowPixel) # , risePct, setPct)

    ledHB.value = not ledHB.value
    time.sleep(sleepTime)
