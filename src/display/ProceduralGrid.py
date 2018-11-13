
import pygame
import noise
from .Grid import Grid
from .Cell import Cell
from . import Color
import random

class ProceduralGrid(Grid):

    def _findCentralNoise(self, abs_pos, r_float):
        x = int((abs_pos[0][0] + abs_pos[1][0])/2)
        y = int((abs_pos[0][1] + abs_pos[1][1])/2)
        scale = 1000
        noiseVal = noise.pnoise3(x/scale, y/scale, r_float, octaves = 8)
        return noiseVal
    
    def __init__(self, surface, width, height, preset = "DEFAULT"):
        super().__init__(surface, width, height)
        self.preset = preset
        r_float  = random.uniform(-1,1)
        for y in range(0, height):
            for x in range(0, width):
                cell     = self.getCell(x, y)
                noiseVal = self._findCentralNoise(cell.abs_pos,r_float)
                color    = None
                if noiseVal < 0:
                    color = Color.BLUE
                elif noiseVal < .03:
                    color = Color.LIGHT_BLUE
                elif noiseVal < .05:
                    color = Color.SAND
                elif noiseVal < .3:
                    color = Color.GREEN
                elif noiseVal < .35:
                    color = Color.GRAY
                else:
                    color = Color.DARK_GRAY
                cell.fill(color)
    

