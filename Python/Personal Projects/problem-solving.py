from tkinter import *
class numberBox:

    def __init__(self, xVal = 255, yVal = 255, zVal = 255):
        self.x = xVal
        self.y = yVal
        self.z = zVal

    def Colorize(self):
        pass





master = Tk()
master.geometry = ('500x500')
bgColor = numberBox(255,0,0)
bgColor.Colorize()
frame = LabelFrame(master, bg = bgColor)
frame.pack()
master.mainloop()

'''def checkEvenInt(num):
    try:
        num1 = int(num)
        if num1 == 0:
            print('0 input error')
        else:
            if num1%2 == 0:
                print('the number is even')
            else:
                print('the number is uneven')

    except ValueError:
        print('Error: input is not compatible with integers')

def checkDeca(num):
    try:
        num1 = int(num)
        if num1 == 0:
            print('0 input error')
        else:
            numOut = num1 // 10
            print()
checkEvenInt(7)'''
