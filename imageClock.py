import os
import time 
import pygame
import random
from datetime import datetime

pygame.init()

display_width = 1600
display_height = 480

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('What Time is it?')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False

path = ("E:/E_Temp/ImageClock/Nixie")

imgList0 = []
imgList1 = []
imgList2 = []
imgList3 = []
imgList4 = []
imgList5 = []
imgList6 = []
imgList7 = []
imgList8 = []
imgList9 = []

for dname in os.listdir(path):
    wrkDir = os.path.join(path, dname)
    j=0
    for fname in os.listdir(wrkDir):
        srcFile = os.path.join(wrkDir, fname)
        print (srcFile)
        img = pygame.image.load(srcFile)
        if dname == "0":
            imgList0.append(img)
        elif dname == "1":
            imgList1.append(img)
        elif dname == "2":
            imgList2.append(img)
        elif dname == "3":
            imgList3.append(img)
        elif dname == "4":
            imgList4.append(img)
        elif dname == "5":
            imgList5.append(img)
        elif dname == "6":
            imgList6.append(img)
        elif dname == "7":
            imgList7.append(img)
        elif dname == "8":
            imgList8.append(img)
        elif dname == "9":
            imgList9.append(img)            
        


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    now = datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")

    hour = int(now.strftime("%H"))
    hour1 = hour%10
    hour10 = int((hour - hour1)/10)

    minute = int(now.strftime("%M"))
    minute1 = minute%10
    minute10 = int((minute - minute1)/10)

    if hour10 == 0: H10 = imgList0[random.randrange(len(imgList0))]
    elif hour10 == 1: H10 = imgList1[random.randrange(len(imgList1))]
    elif hour10 == 2: H10 = imgList2[random.randrange(len(imgList2))]

    if hour1 == 0: H1 = imgList0[random.randrange(len(imgList0))]
    elif hour1 == 1: H1 = imgList1[random.randrange(len(imgList1))]
    elif hour1 == 2: H1 = imgList2[random.randrange(len(imgList2))]
    elif hour1 == 3: H1 = imgList3[random.randrange(len(imgList3))]
    elif hour1 == 4: H1 = imgList4[random.randrange(len(imgList4))]
    elif hour1 == 5: H1 = imgList5[random.randrange(len(imgList5))]
    elif hour1 == 6: H1 = imgList6[random.randrange(len(imgList6))]
    elif hour1 == 7: H1 = imgList7[random.randrange(len(imgList7))]
    elif hour1 == 8: H1 = imgList8[random.randrange(len(imgList8))]
    elif hour1 == 9: H1 = imgList9[random.randrange(len(imgList9))]

    if minute10 == 0: M10 = imgList0[random.randrange(len(imgList0))]
    elif minute10 == 1: M10 = imgList1[random.randrange(len(imgList1))]
    elif minute10 == 2: M10 = imgList2[random.randrange(len(imgList2))]
    elif minute10 == 3: M10 = imgList3[random.randrange(len(imgList3))]
    elif minute10 == 4: M10 = imgList4[random.randrange(len(imgList4))]
    elif minute10 == 5: M10 = imgList5[random.randrange(len(imgList5))]
    elif minute10 == 6: M10 = imgList6[random.randrange(len(imgList6))]
    elif minute10 == 7: M10 = imgList7[random.randrange(len(imgList7))]
    elif minute10 == 8: M10 = imgList8[random.randrange(len(imgList8))]
    elif minute10 == 9: M10 = imgList9[random.randrange(len(imgList9))]

    if minute1 == 0: M1 = imgList0[random.randrange(len(imgList0))]
    elif minute1 == 1: M1 = imgList1[random.randrange(len(imgList1))]
    elif minute1 == 2: M1 = imgList2[random.randrange(len(imgList2))]
    elif minute1 == 3: M1 = imgList3[random.randrange(len(imgList3))]
    elif minute1 == 4: M1 = imgList4[random.randrange(len(imgList4))]
    elif minute1 == 5: M1 = imgList5[random.randrange(len(imgList5))]
    elif minute1 == 6: M1 = imgList6[random.randrange(len(imgList6))]
    elif minute1 == 7: M1 = imgList7[random.randrange(len(imgList7))]
    elif minute1 == 8: M1 = imgList8[random.randrange(len(imgList8))]
    elif minute1 == 9: M1 = imgList9[random.randrange(len(imgList9))]

    gameDisplay.fill(white)
    gameDisplay.blit(H10, (0, 0))
    gameDisplay.blit(H1, (400, 0))
    gameDisplay.blit(M10, (800, 0))
    gameDisplay.blit(M1, (1200, 0))

    pygame.display.update()
    pygame.time.wait(3000)
    # time.sleep(10)


pygame.quit()
quit()
