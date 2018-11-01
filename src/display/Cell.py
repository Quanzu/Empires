import pygame
from . import Color

'''
Logically represents a single "Cell" on a grid.

author:
   Dustin Nguyen

'''

class Cell(object):
    
    def __init__(self, abs_pos, log_pos, surface = None, color = Color.NOT_SET):
        self.abs_pos = abs_pos
        self.log_pos = log_pos
        self.width   = abs_pos[1][0] - abs_pos[0][0] + 1
        self.height  = abs_pos[1][1] - abs_pos[0][1] + 1
        self.surface = surface
        self.color   = color
        if not (color == Color.NOT_SET or surface is None): self.fill(self.color)
        
    def fill(self, color):
        if self.surface is None:
            raise Exception('Cell requires a surface object to fill.')
        for x in range(self.abs_pos[0][0], self.abs_pos[1][0]):
            for y in range(self.abs_pos[0][1], self.abs_pos[1][1]):
                self.surface.set_at((x,y), color)
        self.color = color

    
