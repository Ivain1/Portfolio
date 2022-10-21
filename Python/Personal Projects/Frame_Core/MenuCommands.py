from tkinter import filedialog

def makeNewFile():
    file = open('new.txt', 'w')
    file.write("A new file")

def openExisting():
    targetFile = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("Json files",
                                                     "*.json"),
                                                     ("all files",
                                                      "*.*")))
    contents = open(targetFile, 'r')
    print(contents)
    contents.close()

def saveExisting():
    savefile = contents.get()


def saveNew():
    targetFile = filedialog.asksaveasfile(initialdir="/", title = "Save file As", filetypes = (("Text files", "*txt*"), ("Json files", "*.json*"), ("all files", "*.*")))
    

