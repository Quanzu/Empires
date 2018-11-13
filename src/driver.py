import pygame
import random
import sys
import time
import display.Color as Color
from display.Grid import Grid
from display.ImageGrid import ImageGrid
from display.ProceduralGrid import ProceduralGrid

def main():
    pygame.init()
    res    = 1000,1000
    screen = pygame.display.set_mode(res)
    sizeX  = sizeY = 200
    grid   = Grid(screen, sizeX, sizeY)
    print("here")
    pGrid  = ProceduralGrid(screen,sizeX,sizeY)
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


if __name__=='__main__': main()
