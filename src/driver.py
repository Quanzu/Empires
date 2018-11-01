import pygame
import random
import sys
import time
import display.Color as Color
from display.Grid import Grid
from display.ImageGrid import ImageGrid


def main():
    pygame.init()
    res    = 600,600
    screen = pygame.display.set_mode(res)
    sizeX  = sizeY = 200
    grid   = Grid(screen, sizeX, sizeY)
    imageGrid = ImageGrid('../img/TestMap.png', sizeX,sizeY)
    
    for y in range (0, sizeY):
        for x in range(0, sizeX):
            imageCell = imageGrid.getCell(x, y)
            gridCell  = grid.getCell(x,y)
            gridCell.fill(imageCell.color)

    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            

if __name__=='__main__': main()
