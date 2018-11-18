
import pygame
import noise
from .Grid import Grid
from .Cell import Cell
from . import Color
import random

class ProceduralGrid(Grid):

    def _shiftCellsByAbsPos(self, amount):
        for cell in self.cells:
            x = cell.abs_pos[0][0] + amount
            y = cell.abs_pos[0][1]
            cell.abs_pos = ((x, y), (x + cell.width, y + cell.height))
            cell.fill(cell.color)
            
    def _findNoise(self, pos, scale = 50):
        noiseVal = noise.pnoise3(pos[0]/scale, pos[1]/scale, self.seed, octaves = 8)
        return noiseVal

    def _noiseToColor(self, noiseVal):
        # Temporary solution
        if self.preset == "DEFAULT":
            if   noiseVal <   0: return Color.BLUE
            elif noiseVal < .03: return Color.LIGHT_BLUE
            elif noiseVal < .05: return Color.SAND
            elif noiseVal < .30: return Color.GREEN
            elif noiseVal < .35: return Color.GRAY
            else: return Color.DARK_GRAY

    def __init__(self, surface, width, height, preset = "DEFAULT"):
        super().__init__(surface, width, height)
        self.preset = preset
        self.seed   = random.uniform(-1,1)
        for y in range(0, height):
            for x in range(0, width):
                cell     = self.getCell(x, y)
                noiseVal = self._findNoise(cell.log_pos)
                cell.fill(self._noiseToColor(noiseVal))
                
    def move(self, x = 0, y = 0):
        cellWidth  = int(self.surface.get_width() / self.width)
        cellHeight = int(self.surface.get_width() / self.height)

        print("BEFORE")
        for cell in self.cells:
            print(str(cell))

        
        if (x > 0):            
            self._shiftCellsByAbsPos(-(x * cellWidth))
            for y in range(0, self.height):
                for i in range(0, x):
                    ref_pos  = self.getCell(self.width - x + i, y).abs_pos
                    print("i: {} pos: {}".format(i, (self.width - x + i, y)))
                    abs_pos  = ((ref_pos[0][0] + cellWidth, ref_pos[0][1]), (ref_pos[1][0] + cellWidth, ref_pos[1][1]))
                    c_old    = self.cells.pop(self.width * y + i)
                    log_pos  = (c_old.log_pos[0] + self.width, c_old.log_pos[1] + i)
                    noiseVal = self._findNoise(log_pos)
                    c_new    = Cell(abs_pos, log_pos, surface = self.surface)
                    c_new.fill(self._noiseToColor(noiseVal))
                    #print("inserted into index {}".format(self.width * y + self.width - x + i))
                    self.cells.insert(self.width * y + self.width - x + i, c_new)
            print("AFTER")
            for cell in self.cells:
                print(str(cell))

                                
                    

