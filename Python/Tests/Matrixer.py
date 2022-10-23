"""A testbed for a library on matrices using a co-ordinate system"""

def setMatrix(data,xLeng=int(len(data)),yLeng):
    if yLeng == 0:
        try:
            yLeng == int(yLeng + 1)
        except ValueError:
            print('ValueError, input for yLeng must be a positive integer')



