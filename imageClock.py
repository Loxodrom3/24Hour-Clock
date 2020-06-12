import pygame
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

img0 = pygame.image.load('C:/Users/jproc/Pictures/0.png')
img1 = pygame.image.load('C:/Users/jproc/Pictures/1.png')
img2 = pygame.image.load('C:/Users/jproc/Pictures/2.png')
img3 = pygame.image.load('C:/Users/jproc/Pictures/3.png')
img4 = pygame.image.load('C:/Users/jproc/Pictures/4.png')
img5 = pygame.image.load('C:/Users/jproc/Pictures/5.png')
img6 = pygame.image.load('C:/Users/jproc/Pictures/6.png')
img7 = pygame.image.load('C:/Users/jproc/Pictures/7.png')
img8 = pygame.image.load('C:/Users/jproc/Pictures/8.png')
img9 = pygame.image.load('C:/Users/jproc/Pictures/9.png')
imgList = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    now = datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")
    hour = int(now.strftime("%H"))
    hour = hour%10
    minute = int(now.strftime("%M"))
    minute = minute%10
    print("time:", time)
    print(hour)
    
    
   

    gameDisplay.fill(white)

    gameDisplay.blit(imgList[1], (0, 0))
    gameDisplay.blit(imgList[hour], (400, 0))
    gameDisplay.blit(imgList[1], (800, 0))
    gameDisplay.blit(imgList[minute], (1200, 0))

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
