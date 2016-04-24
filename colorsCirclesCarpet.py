import pygame, sys
import math
import random
from pygame.locals import *

pygame.init()

FPS = 80
fpsClock = pygame.time.Clock()

#set up the window
displWidth = 1200
displHeight = 600
DISPLAYSURF = pygame.display.set_mode((displWidth,displHeight), 0, 32)
pygame.display.set_caption('Fractal')

COLOR = (255,255,255)

def drawCircle(point, radius):
    pygame.draw.circle(DISPLAYSURF, COLOR, point, radius, 1)

c = 0

def drawFractal(center, radius):
    global c
    c = c + 1
    if(radius < 1):
        return
    drawCircle(center, radius)
    global COLOR
    COLOR = ((COLOR[0]+10)%255, (COLOR[1]+10)%255, (COLOR[2]+20)%255)
    drawFractal( (center[0] + radius, center[1]) , radius / 2 )
    drawFractal( (center[0] - radius, center[1]) , radius / 2 )
    drawFractal( (center[0], center[1] + radius) , radius / 2 )
    drawFractal( (center[0], center[1] - radius) , radius / 2 )

drawFractal((displWidth/2,displHeight/2),displWidth)
print c

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
