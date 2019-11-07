import adafruit_ds3231
import time
import board
import simpleio
import neopixel
import digitalio
import math
# below are for oled
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

# SetUp SunRise and SunSet
sunRise = 501, 501, 501, 501, 501, 501, 500, 500, 500, 500, 500, 499, 499, 499, 498, 498, 497, 497, 496, 496, 495, 494, 494, 493, 492, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 474, 473, 472, 471, 469, 468, 467, 465, 464, 463, 461, 460, 458, 457, 456, 454, 453, 451, 450, 448, 447, 445, 444, 442, 440, 439, 437, 436, 434, 433, 431, 429, 428, 426, 425, 423, 421, 420, 418, 417, 415, 413, 412, 410, 409, 407, 405, 404, 402, 401, 399, 397, 396, 394, 393, 391, 390, 388, 387, 385, 384, 382, 381, 379, 378, 376, 375, 373, 372, 371, 369, 368, 366, 365, 364, 363, 361, 360, 359, 358, 356, 355, 354, 353, 352, 351, 350, 349, 348, 347, 346, 345, 344, 343, 342, 341, 341, 340, 339, 338, 338, 337, 336, 336, 335, 335, 334, 334, 333, 333, 333, 332, 332, 332, 332, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 331, 332, 332, 332, 332, 333, 333, 333, 334, 334, 335, 335, 336, 336, 337, 337, 338, 338, 339, 340, 340, 341, 342, 342, 343, 344, 345, 345, 346, 347, 348, 349, 349, 350, 351, 352, 353, 354, 355, 356, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 413, 414, 415, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 446, 447, 448, 449, 450, 451, 452, 453, 455, 456, 457, 458, 459, 460, 461, 463, 464, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 488, 489, 490, 491, 492, 492, 493, 494, 494, 495, 496, 496, 497, 497, 498, 498, 499, 499, 499, 500, 500, 500, 500, 500, 500, 500
sunSet = 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1093, 1094, 1095, 1096, 1097, 1099, 1100, 1101, 1102, 1103, 1105, 1106, 1107, 1108, 1109, 1110, 1112, 1113, 1114, 1115, 1116, 1117, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1216, 1217, 1218, 1219, 1220, 1220, 1221, 1222, 1222, 1223, 1224, 1224, 1225, 1226, 1226, 1227, 1227, 1228, 1228, 1229, 1229, 1229, 1230, 1230, 1230, 1231, 1231, 1231, 1231, 1231, 1231, 1232, 1232, 1232, 1232, 1232, 1231, 1231, 1231, 1231, 1231, 1231, 1230, 1230, 1230, 1229, 1229, 1228, 1228, 1227, 1227, 1226, 1226, 1225, 1225, 1224, 1223, 1222, 1222, 1221, 1220, 1219, 1218, 1217, 1216, 1215, 1214, 1213, 1212, 1211, 1210, 1209, 1208, 1207, 1205, 1204, 1203, 1202, 1201, 1199, 1198, 1197, 1195, 1194, 1193, 1191, 1190, 1188, 1187, 1185, 1184, 1182, 1181, 1179, 1178, 1176, 1175, 1173, 1172, 1170, 1169, 1167, 1165, 1164, 1162, 1161, 1159, 1157, 1156, 1154, 1152, 1151, 1149, 1148, 1146, 1144, 1143, 1141, 1139, 1138, 1136, 1134, 1133, 1131, 1129, 1128, 1126, 1125, 1123, 1120, 1118, 1117, 1115, 1113, 1112, 1110, 1109, 1107, 1106, 1104, 1103, 1101, 1100, 1098, 1097, 1095, 1094, 1092, 1091, 1090, 1088, 1087, 1086, 1084, 1083, 1082, 1081, 1079, 1078, 1077, 1076, 1075, 1074, 1073, 1072, 1071, 1070, 1069, 1068, 1067, 1066, 1065, 1064, 1063, 1063, 1062, 1061, 1061, 1060, 1059, 1059, 1058, 1058, 1057, 1057, 1057, 1056, 1056, 1056, 1055, 1055, 1055, 1055, 1055, 1055, 1055, 1055, 1055, 1055, 1055, 1055, 1056, 1056, 1056, 1056, 1057, 1057, 1058, 1058, 1059, 1059, 1060, 1060, 1061, 1062, 1062, 1063, 1064, 1064, 1065, 1065, 1065
monthDay = 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334  # since RTC are not supporting dayOfYear, I am using this for calculating the number of days pass by the month.
toDay = 0
currMin = 0
DLS = -60  # Day Light Savings.  Set to 0 for no adjustment, and -60 for DLS

# SetUp HeartBeat
ledHB = digitalio.DigitalInOut(board.D13)
ledHB.direction = digitalio.Direction.OUTPUT
ledHB.value = True

# SetUp NeoPixels
LEDPin = board.A1
numLED = 24
ORDER = neopixel.RGB
ringLED = neopixel.NeoPixel(LEDPin, numLED, brightness=0.2, auto_write=False, pixel_order=ORDER)

base = 1440  # Seconds in a Day

dayR = 45
dayG = 30
dayB = 0
nitR = 0
nitG = 10
nitB = 50
minR = 0
minG = 250
minB = 0
redBase = min(dayR, nitR)
grnBase = min(dayG, nitG)
bluBase = min(dayB, nitB)
redList=[0 for i in range(numLED)]
grnList=[0 for i in range(numLED)]
bluList=[0 for i in range(numLED)]
whtList=[0 for i in range(numLED)]
whtList[00]=50
whtList[int(numLED/2)]=100

font = terminalio.FONT
displayio.release_displays()

i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
oled = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

rtc = adafruit_ds3231.DS3231(i2c)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# if False:   # change to True if you want to write the time!
    #                       year, mon, date, hour, min, sec, wday, yday, isdst
    # t = time.struct_time((2019,  11,   28,   00,  13,  45,    0,   -1,    -1))
    # rtc.datetime = t
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

# set up Text label
text_display = "Denver Time"
clock_group = displayio.Group()


while True:
    current = rtc.datetime
    minOfDay = (((current.tm_hour+12)%24)*60) + current.tm_min + DLS
    dayOfYear = monthDay[current.tm_mon - 1] + current.tm_mday  # using '- 1' because Jan is month 1, and index for monthDay starts at 0

    if toDay != dayOfYear:
        toDay = dayOfYear

    # Only calculate color when minute increments

    if currMin != minOfDay:
        currMin = minOfDay
        setPixel = int((numLED*(sunSet[toDay] + DLS)/base) - (numLED / 2))
        risePixel = int((numLED*(sunRise[toDay] + DLS)/base) + (numLED / 2)) - 1  # should use ceiling
        setPct = ((numLED*(sunSet[toDay] + DLS)/base) - (numLED / 2)) - setPixel
        risePct = ((numLED*(sunRise[toDay] + DLS)/base) + (numLED / 2)) - 1 - risePixel
        if dayR > nitR:
            setR = redBase + int((setPct  * abs(dayR - nitR)))
            riseR = redBase + int((1-risePct) * abs(dayR - nitR))
        else:
            setR = redBase + int(((1-setPct)  * abs(dayR - nitR)))
            riseR = redBase + int(risePct * abs(dayR - nitR))
        if dayG > nitG:
            setG = grnBase + int(((setPct) * abs(dayG - nitG)))
            riseG = grnBase + int((1-risePct) * abs(dayG - nitG))
        else:
            setG = grnBase + int(((1-setPct) * abs(dayG - nitG)))
            riseG = grnBase + int(risePct * abs(dayG - nitG))
        if dayB > nitB:
            setB = bluBase + int((setPct * abs(dayB - nitB)))
            riseB = bluBase + int((1-risePct) * abs(dayB - nitB))
        else:
            setB = bluBase + int(((1-setPct) * abs(dayB - nitB)))
            riseB = bluBase + int(risePct * abs(dayB - nitB))
        # set colors for redList, grnList, bluList
        for i in range(0, setPixel, 1):
            redList[i] = dayR
            grnList[i] = dayG
            bluList[i] = dayB
        redList[setPixel] = setR
        grnList[setPixel] = setG
        bluList[setPixel] = setB
        for i in range(setPixel + 1, risePixel, 1):
            redList[i] = nitR
            grnList[i] = nitG
            bluList[i] = nitB
        redList[i] = riseR
        grnList[i] = riseG
        bluList[i] = riseB
        for i in range(risePixel, numLED, 1):
            redList[i] = dayR
            grnList[i] = dayG
            bluList[i] = dayB
        # assign minute to pixel
        minPixel = int((currMin / base) * numLED)
        minPct = ((currMin / base) * numLED) - minPixel
        if minR > redList[minPixel%numLED]:
            redList[minPixel+1] = min(minR, redList[minPixel]) + int(minPct  * abs(minR - redList[minPixel]))
            redList[minPixel] = min(minR, redList[minPixel]) + int((1-minPct) * abs(minR - redList[minPixel]))
        else:
            redList[minPixel+1] = min(minR, redList[minPixel]) + int((1-minPct)  * abs(minR - redList[minPixel]))
            redList[minPixel] = min(minR, redList[minPixel]) + int(minPct * abs(minR - redList[minPixel]))
        if minG > grnList[minPixel]:
            grnList[minPixel+1] = min(minG, grnList[minPixel]) + int(minPct  * abs(minG - grnList[minPixel]))
            grnList[minPixel%numLED] = min(minG, grnList[minPixel]) + int((1-minPct) * abs(minG - grnList[minPixel]))
        else:
            grnList[(minPixel+1)%numLED] = min(minG, grnList[minPixel]) + int((1-minPct)  * abs(minG - grnList[minPixel]))
            grnList[minPixel] = min(minG, grnList[minPixel]) + int(minPct * abs(minG - grnList[minPixel]))
        if minB > bluList[minPixel]:
            bluList[(minPixel+1)%numLED] = min(minB, bluList[minPixel]) + int((1-minPct)  * abs(minB - bluList[minPixel]))
            bluList[minPixel] = min(minB, bluList[minPixel]) + int(minPct * abs(minB - bluList[minPixel]))
        # else:
            # do that
            # and that

    for i  in range (0, numLED, 1):
        ringLED[i] = (redList[i], grnList[i], bluList[i])

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

    # print(current.tm_mon, current.tm_mday, monthDay[current.tm_mon -1], dayOfYear, toDay, sep=", ")
    # print((ring1*sunSet[toDay]/base) - (ring1 / 2), setPixel, setPct, ((ring1*sunRise[toDay]/base) + (ring1 / 2)) - 1, risePixel, risePct, sep=", ")
    # print(dayR, dayG, dayB, " ", nitR, nitG, nitB, sep = ", ")
    # print(setR, setG, setB, " ", riseR, riseG, riseB, sep = ", ")
    print(sunRise[toDay], sunSet[toDay], sep=", ")
    print(toDay, time_display, currMin, minOfDay, minPixel, minPct, sep=", ")

    # show results and sleep
    oled.show(clock_group)
    ringLED.show()
    ledHB.value = not ledHB.value  # toggel the heart beat LED to let us know it is running
    time.sleep(0.1)
