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

WHITE = (255,255,255    )

def drawCircle(point, radius):
    pygame.draw.circle(DISPLAYSURF, WHITE, point, radius, 1)

def drawFractal(center, radius):
    if(radius < 1):
        return
    drawCircle(center, radius)
    drawFractal( (center[0] + radius, center[1]) , radius / 2 )
    drawFractal( (center[0] - radius, center[1]) , radius / 2 )

while True:
    drawFractal((displWidth/2,displHeight/2),displWidth)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
