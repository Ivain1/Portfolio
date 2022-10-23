from tkinter import *

class Cell:
    def __init__(self,master,x,y):
        self.width = 10
        self.height = 1
        self.x = x
        self.y = y
        self.content = '{0}{1}'.format(self.x,self.y)
        self.m = master
        self.m.geometry('800x800')
        label = Label(self.m, width=self.width, height=self.height, bg='lightblue',
                           text='{0},{1}'.format(self.x, self.y), bd=10)
        label.grid(column=x, row=y)



root = Tk()
for x in range(9):
    for y in range(9):
        Cell_1 = Cell(root,x,y)




root.mainloop()


