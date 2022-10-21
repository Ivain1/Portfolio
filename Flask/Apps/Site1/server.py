# app.py
from flask import Flask, render_template, make_response  # importing the render_template function
from random import randint
import datetime
import os

def shuffle(o_list):
    list_len = len(o_list)
    for i in range(list_len):
        entry = o_list.pop(i)
        ind = randint(0,list_len)
        o_list.insert(ind,entry)
    print(o_list)

o_list = ['a','b','c','d']
shuffle(o_list)



app = Flask(__name__)
IMG_FOLDER = os.path.join('static','IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

# home route

@app.route("/index.html")

def index():
    project_img = os.path.join(app.config['UPLOAD_FOLDER'], 'image1.png')
    time = datetime.datetime.now()
    calendar = time.strftime("%A %d %B %Y")
    clock = time.strftime("%H:%M")
    timezone = time.strftime("%z, %Z")
    number = randint(0,100)
    #article = str(open("article-1.txt"))
    return render_template('index.html',name='Jorn Hiemstra', age='26', num=number, clock=clock, calendar=calendar, user_image=project_img)

@app.route("/aboutme.html")
def aboutme():
    time = datetime.datetime.now()
    calendar = time.strftime("%A %d %B %Y")
    clock = time.strftime("%H:%M")
    timezone = time.strftime("%z, %Z")

    return render_template('aboutme.html',name='Jorn Hiemstra', age='26')

@app.route("/gallery.html")
def gallery():
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], 'image1.png')
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'image2.png')
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'image3.png')
    img4 = os.path.join(app.config['UPLOAD_FOLDER'], 'image4.png')
    img5 = os.path.join(app.config['UPLOAD_FOLDER'], 'image5.png')

    return(render_template('gallery.html',G1 = img1,G2 = img2, G3 = img3, G4 = img4, G5 = img5))
@app.route("/contact.html")
def contact():
    return render_template('contact.html')
app.run(debug = True)