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
root.geometry('800x800')


dataset = []

for i in range(0,100):
    dataset.append(randint(0,100))
print(dataset)



def gridlines(width,height,gridsize):
    C = Canvas(root, bg='light gray', width=width, height=height)
    xNum = int(width/gridsize)
    yNum = int(height/gridsize)
    graphgrid = []

    for i in range(0,xNum):
        line = C.create_line(i*xNum, 0, i*xNum, height, width=1, fill='red')

    for i in range(0,yNum):
        line = C.create_line(0, i*yNum, width, i*yNum, width=1, fill='blue')

    print(graphgrid)
    C.pack()




def lineGraph(width,height,data):
    C = Canvas(root, bg="light gray", width=width, height=width)
    lineX1 = 0
    lineX2 = 0
    lineY1 = 0
    lineY2 = 0
    length = len(data)
    steps = width/length
    for i in range(0,length):
        lineX2 = lineX2 + steps*i
        print(lineX2)
        lineY2 = data[i]
        print(lineY2)
        C.create_line(lineX1,lineY1,lineX2,lineY2, width=5, fill='blue')
        lineX1 = lineX2
        lineY1 = lineY2
    C.pack(fill=BOTH, expand=True)
#lineGraph(200,200,dataset)
gridlines(500,500,16)








mainloop()
