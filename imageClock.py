import pygame
from datetime import datetime

pygame.init()


display_width = 1200
display_height = 300

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

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
imgList = ['img0','img1','img2','img3','img4','img5','img6','img7','img8','img9']

def hr10(img, x, y):
    gameDisplay.blit(img, (x, y))

def hr1(img, x, y):
    gameDisplay.blit(img, (x, y))

def mn10(img, x, y):
    gameDisplay.blit(img, (x, y))

def mn1(img, x, y):
    gameDisplay.blit(img, (x, y))

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    now = datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")
    print("time:", time)

    gameDisplay.fill(white)
    hr10(img1, 0, 0)
    hr1 (img7, 300, 0)
    mn10 (img4, 600, 0)
    mn1 (img6, 900, 0)
        
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
quit()
