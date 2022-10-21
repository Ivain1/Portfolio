from tkinter import *
from UI_Classes import *
from MenuCommands import *

WIDTH = 1024
HEIGHT = 768
size_string = str(WIDTH) + 'x' + str(HEIGHT)
master = Tk()
master.geometry(size_string)
smokeGray = smokeGray()
darksmokeGray = darksmokeGray()
titleFont = titleFont(64)
H1 = H1()
master.configure(bg = smokeGray)

pw = PanedWindow(master, orient = 'horizontal')


#outerFrame = LabelFrame(pw, bg = 'dark gray', fg = 'gainsboro', bd = 0)
innerFrame = LabelFrame(pw, bg = smokeGray, fg = 'gainsboro', bd = 0)
sideFrame = LabelFrame(pw, bg = darksmokeGray, fg = 'gainsboro', bd = 0)
centerFrame = LabelFrame(pw, bg = smokeGray, fg = 'gainsboro', bd = 0)
#outerFrame.pack(fill = BOTH, expand = True, padx = 5, pady = 5)
innerFrame.pack(fill = BOTH, expand = True, padx = 5, pady = 5,side = RIGHT)
sideFrame.pack(fill = BOTH, expand = True, padx = 5, pady = 5, side = LEFT)
centerFrame.place(relx = 0.5, rely = 0.5, anchor = 'center')
title = Label(sideFrame, text = 'Left', bg = smokeGray, fg = 'gainsboro', font =H1)
title2 = Label(innerFrame, text = 'Right', bg = smokeGray, fg = 'gainsboro', font =H1)
title3 = Label(centerFrame, text = 'Center', bg = smokeGray, fg = 'gainsboro', font = H1)
title.pack(fill = BOTH, expand = True)
title2.pack(fill = BOTH, expand = True)
title3.pack(fill = BOTH, expand = True)

pw.add(innerFrame)
pw.add(centerFrame)
pw.add(sideFrame)

pw.place(relx = 0.5, rely = 0.5, anchor = 'center')
pw.configure(sashrelief = RAISED)


menubar = Menu(master)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = file)
file.add_command(label = 'New File', command = makeNewFile)
file.add_command(label = 'Open', command = openExisting)
file.add_command(label = 'Save', command = saveExisting)
file.add_command(label = 'Save as', command = saveNew)




master.config(menu = menubar)
master.mainloop()