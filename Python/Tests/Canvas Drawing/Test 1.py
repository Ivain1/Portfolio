from tkinter import *
from random import randint
cWIDTH = 1000
cHEIGHT = 1000
lineX1 = 1
lineX2 = 100
lineY1 = 1
lineY2 = 100
lineWidth = 5
i=0
root = Tk()

C = Canvas(root, bg = "light gray", width = cWIDTH, height=cHEIGHT)
def randomizer(min,max):
    randomNumber = randint(min,max)
    print(randomNumber)
    return(randomNumber)
while lineX1 <= 1000 and lineY1 <= 1000:
    i = i+1
    lineX2 = lineX1 + 50
    lineY2 = lineY1 + randomizer(5, 25) * (1 + (i / 5))
    #lineX1 = randomizer(0,100)
    #lineY1 = randomizer(0,100)
    #lineX2 = randomizer(20,200)
    #lineY2 = randomizer(20,200)

    line = C.create_line(lineX1, lineY1, lineX2, lineY2, width = lineWidth, fill = "blue")
    lineX1 = lineX2
    lineY1 = lineY2
    columnX = lineX2
    columnY = cHEIGHT
    C.create_rectangle(columnX,columnY,lineX2,lineY2, fill='lightblue')


C.pack()
mainloop()
