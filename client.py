#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def musicWindow():

    #Client GUI starts here
    window=Tk()
    window.title('Music Windowc')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectlabel = Label(window, text= "Select Song", font = ("Calibri",10))
    selectlabel.place(x=2, y=1)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    connectserver = Button(window,text="Connect to Chat Server",bd=1, font = ("Calibri",10))
    connectserver.place(x=350,y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', bg='LightSkyBlue', font = ("Calibri",10))
    listbox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    PlayButton=Button(window,text="Play", bg='SkyBlue', width=10, bd=1, font = ("Calibri",10))
    PlayButton.place(x=30,y=200)

    stop=Button(window,text="Stop", bg='SkyBlue', width=10, bd=1, font = ("Calibri",10))
    stop.place(x=200,y=200)

    upload=Button(window,text="Refresh",bd=1, font = ("Calibri",10))
    upload.place(x=30,y=250)
  
    download = Button(window,text="Download",bd=1, font = ("Calibri",10))
    download.place(x=200, y=250)

    infoLabel = Label(window, text="",fg="blue", font=("Calibri", 10))
    infoLabel.place(x=4,y= 280)


    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()
