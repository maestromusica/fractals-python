import pygame, sys
import math
import pygame.gfxdraw
import random
from pygame.locals import *

pygame.init()

FPS = 80
fpsClock = pygame.time.Clock()

#set up the window
displWidth = 1600
displHeight = 1000
DISPLAYSURF = pygame.display.set_mode((displWidth,displHeight), 0, 32)
pygame.display.set_caption('Fractral')

COLOR = (255,255,255)

center = (displWidth/2, displHeight/2)
radius = displHeight / 2;

def randColor():
    return ( int(random.random()*255),  int(random.random()*255),  int(random.random()*255))

def drawCircle(point, radius):
    x,y=point
    pygame.gfxdraw.aacircle(DISPLAYSURF, x,y, int(radius), COLOR)

while True:
    drawCircle(center, radius)
    if(radius > 5):
        radius *= 0.99
        COLOR = ((COLOR[0]+5)%255,(COLOR[1]+5)%255,(COLOR[2]+5)%255)
    else:
        radius = displHeight / 2;
        COLOR = randColor()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
