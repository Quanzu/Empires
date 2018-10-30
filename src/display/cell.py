import pygame

'''
Logically represents a single "Cell" on a grid.

author:
   Dustin Nguyen

'''

class Cell(object):
    
    def __init__(self, abs_pos, log_pos):
        self.abs_pos = abs_pos
        self.log_pos = log_pos
        self.width   = abs_pos[1][0] - abs_pos[0][0] + 1
        self.height  = abs_pos[1][1] - abs_pos[0][1] + 1

    def fill(self, surface, color):
        for x in range(self.abs_pos[0][0], self.abs_pos[1][0]):
            for y in range(self.abs_pos[0][1], self.abs_pos[1][1]):
                surface.set_at((x,y), color)
        return surface

