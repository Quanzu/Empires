import uuid
from .Grid import Grid
from .Cell import Cell
from .     import Color
from PIL   import Image

class ImageGrid(Grid):


    def saveImage(self):
        fn = str(uuid.uuid4())
        self.img.save("../img/" + fn + ".png" , format = "PNG")
        
    
    def _findModeColor(self, abs_pos):
        colorMap   = {}
        modeColor  = (Color.NOT_SET, 0)
        cellWidth  = abs_pos[1][0] - abs_pos[0][0]
        cellHeight = abs_pos[1][1] - abs_pos[0][1]
        majority   = int((cellWidth * cellHeight)/2)
    
        for y in range(abs_pos[0][1], abs_pos[1][1]):
            for x in range(abs_pos[0][0], abs_pos[1][0]):
                try:
                    color = self.pixel_vals[self.imgWidth * y + x]
                    if color in colorMap: colorMap[color] += 1
                    else: colorMap.update({color : 1})
                    if colorMap[color] >= modeColor[1]: modeColor = (color, colorMap[color])  
                    if modeColor[1] >= majority: break
                except: break
        return modeColor[0]
    
    
    def _makeImageDivisable(self):
        self.img = self.img.resize((self.imgWidth - (self.imgWidth % self.width), self.imgHeight - (self.imgHeight % self.height)), Image.BILINEAR)
        self.imgWidth, self.imgHeight = self.img.size
        self.saveImage()
    
    def __init__(self, img, width, height):
        if width <= 0 or height <= 0: raise Exception("Width and height cannot be less than or equal to 0.")
        
        self.img = Image.open(img, 'r')
        self.cells  = []
        self.width  = width
        self.height = height
        self.imgWidth, self.imgHeight = self.img.size

        if int(self.imgWidth / width) == 0 or int(self.imgHeight / height) == 0:
            raise Exception("Image of size {} by {} is too small to be divided into a {} by {} grid.".format(imgWidth, imgHeight, width, height))
        
        if self.imgWidth % width != 0 or self.imgHeight % height != 0:
            self._makeImageDivisable()
            
        self.pixel_vals = list(self.img.getdata())

        cellWidth  = int(self.imgWidth  / width)
        cellHeight = int(self.imgHeight / height)

        for y in range(0, self.imgHeight, cellHeight):
            for x in range(0, self.imgWidth, cellWidth):
                abs_pos = ((x, y),(x + cellWidth, y + cellHeight))
                log_pos = (int(x / cellWidth), int(y / cellHeight))
                color = self._findModeColor(abs_pos)
                c = Cell(abs_pos, log_pos, color = color)
                self.cells.append(c)

