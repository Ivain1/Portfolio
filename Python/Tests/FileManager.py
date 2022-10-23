from tkinter import *
from tkinter import filedialog

pathStorage = []
#shortcutName = ""
filecount = 0
#filename = 'file' + str(filecount)
def browseFiles():
    global filecount
    filename = 'file' + str(filecount)
    targetfile = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    labeltext = str("File Opened: " + targetfile +'\n'+ str(pathStorage))
    label_file_explorer.configure(text = labeltext)
    pathStorage.append() = targetfile
    filecount = filecount + 1
    print(filecount)
    print(pathStorage)




window = Tk()

window.title('File Explorer')

window.geometry("500x500")

window.config(background = "white")

label_file_explorer = Label(window, text = "File Explorer using Tkinter", width = 72, height = 4, fg = "dark blue")


button_explore = Button(window, text = "Browse Files", command = browseFiles)
button_exit = Button(window, text = "Exit", command = exit)


label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1, row = 3)


window.mainloop()
