from random import randint
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

class UI:
    def __init__(self,root,w=500,h=600):
        self.root = root
        self.geometry = self.root.geometry('{0}x{1}'.format(w,h))
        self.titleframe = Frame(self.root,bg='dimgray')
        self.main_title = Label(self.root,text='UI Title', font=('Verdana',20), bg='dark gray', fg='gainsboro')
        self.frame1 = Frame(self.root,bg='red')
        self.frame2 = Frame(self.root,bg='green')
        self.frame3 = Frame(self.root,bg='blue')

        self.button1 = Button(self.frame1, bg='darkred', fg='gainsboro', text='Choose Red',
                              command=lambda: data_update('red'))
        self.button2 = Button(self.frame2, bg='darkgreen', fg='gainsboro', text='Choose Green',
                              command=lambda: data_update('green'))
        self.button3 = Button(self.frame3, bg='darkblue', fg='gainsboro', text='Choose Blue',
                              command=lambda: data_update('blue'))

        self.main_title.pack(fill=BOTH, expand=False)
        self.frame1.pack(fill=BOTH,expand=True)
        self.frame2.pack(fill=BOTH,expand=True)
        self.frame3.pack(fill=BOTH,expand=True)

        self.button1.pack(fill=BOTH,expand=True,padx=5,pady=5)
        self.button2.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.button3.pack(fill=BOTH, expand=True, padx=5, pady=5)


class Data:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def __str__(self):
        return("Red:{0}\nGreen: {1}\nBlue: {2}".format(self.red,self.green,self.blue))

    def red_add(self):
        self.red += 1

    def green_add(self):
        self.green += 1

    def blue_add(self):
        self.blue += 1
    def output(self):
        return([self.red,self.green,self.blue])


root = Tk()
r = UI(root,1000,800)
Data = Data()


def main():
    #create_ui()
    #data_update()
    data_process()
    data_display()





def data_update(choice):
    if choice == 'red':
        Data.red_add()
    elif choice == 'green':
        Data.green_add()
    elif choice == 'blue':
        Data.blue_add()
    else:
        print('Not a valid choice')


def data_process():
    pass

def data_display():
    plt.bar(('red','green','blue'),Data.output(),color=('red','green','blue'))
    plt.show()
    print(Data)

root.after(5000, main)
root.mainloop()