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
    res    = 600,600
    screen = pygame.display.set_mode(res)
    sizeX  = sizeY = 100
    pGrid  = ProceduralGrid(screen,sizeX,sizeY)
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("UP")
                elif event.key == pygame.K_DOWN:
                    print("DOWN")
                elif event.key == pygame.K_LEFT:
                    print("LEFT")
                elif event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    pGrid.move(x=10, y=0)
                    pygame.display.flip()
                    
if __name__=='__main__': main()
