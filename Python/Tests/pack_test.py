from tkinter import *

window = Tk()
window.title("Pack Problem")

windowWidth = 1000
windowHeight = 500
windowSize = str(windowWidth) + "x" + str(windowHeight)
window.geometry(windowSize)

frame = Frame()
frame.pack(side=BOTTOM, anchor = W)

bottone_reset = Button(frame,text = "reset")
bottone_premi = Button(frame, text = "premi")
etichetta_click = Label(frame, text = "click")
etichetta_titolo = Label(frame, text = "Title")

bottone_reset.configure(width = 10, height = 3, bg = 'light gray', fg = 'black')
bottone_premi.configure(width = 10, height = 3, bg = 'light gray', fg = 'black')
etichetta_click.configure(width = 10, height = 3, bg = 'light gray', fg = 'black')
etichetta_titolo.configure(width = 10, height = 3, bg = 'light gray', fg = 'black')


def padsize(e):


    if e.height <= 1080 and e.height > 768:
        bottone_reset.grid(column=0, row=0, padx=25, pady=25)
        bottone_premi.grid(column=1, row=0, padx=25, pady=25)
        etichetta_click.grid(column=2, row=0, padx=25, pady=25)
        etichetta_titolo.grid(column=3, row=0, padx=25, pady=25)
        #print("window height is larger than 768")
    elif e.height <768 and e.height > 640:
        bottone_reset.grid(column=0, row=0, padx=15, pady=15)
        bottone_premi.grid(column=1, row=0, padx=15, pady=15)
        etichetta_click.grid(column=2, row=0, padx=15, pady=15)
        etichetta_titolo.grid(column=3, row=0, padx=15, pady=15)
        #print("window height is larger than 768")
    elif e.height <640 and e.height > 250:
        bottone_reset.grid(column=0, row=0, padx=5, pady=5)
        bottone_premi.grid(column=1, row=0, padx=5, pady=5)
        etichetta_click.grid(column=2, row=0, padx=5, pady=5)
        etichetta_titolo.grid(column=3, row=0, padx=5, pady=5)
        #print("window height is smaller than 768")



#bottone_reset.grid(column = 0, row = 0, padx = 5 , pady = 5)
#bottone_premi.grid(column = 1, row = 0, padx = 5, pady = 5)
#etichetta_click.grid(column = 2, row = 0, padx = 5, pady = 5)
#etichetta_titolo.grid(column = 3, row = 0, padx = 5, pady = 5)

window.bind('<Configure>', padsize)

window.mainloop()
