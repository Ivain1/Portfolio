#import array as arr
maxheight = 255
global maxheight

class PixelData:
    def __init__(self, pixelX, pixelY, pixelHeight, pixelType):
        self._pixelX = pixelX
        self._pixelY = pixelY
        self._pixelH = pixelHeight
        self._pixelT = pixelType



    def change_height(self, heightAddition):
        self._pixelH = self._pixelH + heightAddition
        if self._pixelH > maxHeight:
            self._pixelH = maxHeight

    def change_type(self, newType):
        self._pixelT = newType




