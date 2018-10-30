import pygame
import random
import sys
from display.grid import Grid


WHITE = (255,255,255)
RED = (255, 0, 0)
def main():
    pygame.init()
    res = 600,600
    screen = pygame.display.set_mode(res)
    
    grid = Grid(screen, 10, 10)

    for cell in grid.cells:
        r = random.randint(0,1)
        if r == 0:
            cell.fill(screen, WHITE)
        
    
    cell = grid.getCell(3,2)
    cell.fill(screen, RED)
    print("Got cell with coordinates: " + str(cell.log_pos))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            

if __name__=='__main__': main()
