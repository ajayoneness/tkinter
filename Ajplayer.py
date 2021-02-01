from tkinter import *
from playsound import playsound
import os
root= Tk()
def play():
    playsound("C:\\Users\\Hacking knowledge\\Desktop\\songs\\a (1).mp3")
def allsong1(): 
    allsong=os.listdir("C:\\Users\\Hacking knowledge\\Desktop\\songs")
    print("LIST OF SONGS ")
    verticaltable="\n".join(allsong)
    print (verticaltable)
            
def push():
    pass

root.title("Aj player")
root.geometry("245x400")
f1=Frame(root,bg="yellow4",padx="7",borderwidth= "6")
f1.pack(side=LEFT,fill="y")

b1=Button(f1,text="all song",bg="yellow1",fg="gray",padx="10",pady="10",font="arial 10 bold",borderwidth="10",command=allsong1)
b1.pack(side=LEFT)
b2=Button(f1,text="stop",bg="yellow1",fg="gray",padx="10",pady="10",font="arial 10 bold",borderwidth="10")
b2.pack(side=LEFT)
b3=Button(f1,text="play",bg="yellow1",fg="gray",padx="10",pady="10",font="arial 10 bold",borderwidth="10",command=play)
b3.pack(side=LEFT)

root.mainloop()
