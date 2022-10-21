from random import randint

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.options = [0,1,2,3,4,5,6,7,8,9]
        self.center = True #effectively a variable to keep track of whether or not a tile is on the edge of the grid.
        self.east = True
        self.west = True
        self.north = True
        self.south = True



    def posCheck(self, xMax = 2, yMax = 2):
        '''
        Takes the maximum X and Y range of the grid as input. A 3x3 grid is the minimum size, so the default xMax value is 2 (arrays start at 0)
        :param xMax:
        :param yMax:
        :return:
        '''
        if self.x == 0 or self.x == xMax or self.y == 0 or self.y == yMax: #If the coordinates of the cell/tile are 0 or the max range of either axis, then the tile CANNOT become the center type
            self.center = False
        if self.x == 0:
            self.west = True
            self.east = False

        if self.y == 0:
            self.north = True
            self.south = False

        if self.x == xMax:
            self.east = True
            self.west = False

        if self.y == yMax:
            self.south = True
            self.north = False

def gridSetup(xSize = 9, ySize = 9, options = ['a','b','c','d','e','f','g','h','i']):
    xLen = xSize
    yLen = ySize
    xlist = []
    ylist = []
    for i in range(0,(yLen-1)):

        for i in range(0,(xLen-1)):
            xlist.append(options)
        ylist.append(xlist)

    print(ylist)
    return(ylist)

def Collapse(grid,start_pos, options):
    choice = randint(0,(len))

gridSetup()


