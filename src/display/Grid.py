import pygame
from .Cell import Cell

'''
Logically seperates a surface into a grid of x by x sized cells

author:
   Dustin Nguyen

'''

class Grid(object):
    
    def __init__(self, surface, width, height):
        
        if width <= 0 or height <= 0:
            raise Exception("width and height cannot be less than or equal to 0.")
        
        self.surface = surface # Surface that this grid will logically divide
        self.cells   = []      # 1D list of cells
        self.width   = width
        self.height  = height
        
        cellWidth  = int(self.surface.get_width()  / width)
        cellHeight = int(self.surface.get_height() / height)
        
        for y in range(0, self.surface.get_height(), cellHeight):
            for x in range(0, self.surface.get_width(), cellWidth):
                abs_pos = ((x, y),(x + cellWidth, y + cellHeight))
                log_pos = (int(x / cellWidth), int(y / cellHeight))
                c = Cell(abs_pos, log_pos, surface = self.surface)
                self.cells.append(c)
                
    def getCell(self, x, y):
        if x < 0 or x > self.width-1:
            raise Exception("x should be within bounds of 0 <= x <= {}".format(self.width-1))
        if y < 0 or y > self.height-1:
            raise Exception("y should be within bounds of 0 <= y <= {}".format(self.height-1))
        return self.cells[self.width * y + x]
