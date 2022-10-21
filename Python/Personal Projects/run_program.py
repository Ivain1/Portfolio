import subprocess
import os
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog


global jar_path
global jar_name
jar_path = 'C:/Users/Ivain/Desktop/1.18 Server/1.19/Test1/'

m = Tk()
style = Style()
width = 640
height = 720
window_size = '{0}x{1}'.format(width,height)
m.geometry(window_size)
style.configure('Tbutton', font=('Verdana', 14, 'bold'), fg = 'red', bg = 'purple')

def find_jar(old_path):
    global jar_path
    new_jar = filedialog.askopenfilename(initialdir="/",
                                         title="Select the new Jar file",
                                         filetypes = (("Jar files",
                                                       "*.jar*"),
                                                      ('Batch files',
                                                       '*.bat*'),
                                                      ("all files",
                                                       "*.*")))
    jar_dir.configure(text=new_jar)
    jar_path = new_jar.replace(" ", "_")
    old_path = new_jar.replace(" ", "_")
    return(old_path)



style.map('TButton', foreground = [('active', 'darkgray')]
                   , background = [('active', 'gainsboro')])
c_frame = Frame(m,bg = 'darkgray')

inner_frame = Frame(c_frame,bg = 'gray')

title = Label(inner_frame,text='Local Server Manager',font = ('Verdana',32), fg = 'gainsboro', bg = 'gray')

hr = Frame(inner_frame,bg = 'gainsboro', height=4, width = (width-64))
jar_dir = Label(inner_frame, text = jar_path , padx = 10, pady = 3, width = int(width/10))
jar_ask = ttk.Button(inner_frame, text = 'Open Directory', style= 'TButton', command = lambda: find_jar(jar_path))


c_frame.pack(fill = BOTH, expand = True)
inner_frame.pack(fill=BOTH,expand=True,padx=7,pady=7)
title.grid(column = 0, row = 0, sticky = N,padx = 64, columnspan = 2)
hr.grid(column = 0, row = 1, sticky = N, columnspan = 2)
jar_ask.grid(column = 0, row = 2, sticky = E, pady = 20, padx = 5)
jar_dir.grid(column = 1, row = 2, sticky = W, columnspan = 1)
jar_path = str(jar_dir['text'])
print(jar_path)

def server_start(path = jar_path):
    print(path)
    try:
        os.system(path)
        #subprocess.call(['javaw', '-jar', path])
    except TimeoutError:
        print('The server took too long to start')

start_server = ttk.Button(inner_frame, text = 'Start Server', style = 'TButton', command = lambda:server_start(jar_path))
start_server.grid(column = 0, row = 3,sticky = E)


#server_start()





if __name__ == '__main__':
    m.mainloop()
#  import os
#os.chdir('C:/Users/Ivain/Desktop/1.18 Server/1.19/Test1/',["@echo off"])
#os.startfile("start.bat")

'''import subprocess
from subprocess import Popen
filepath="C:/Users/Ivain/Desktop/1.18 Server/1.19/Test1/start.bat"
p = Popen(filepath, shell=True, stdout = subprocess.PIPE)
stdout, stderr = p.communicate()

print(p.returncode)

'''