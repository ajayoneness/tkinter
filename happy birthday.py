from tkinter import *
import time
import playsound
#BORDER STYLE(relief)= SUNKEN, RAISED, GROOVE, RIDGE
for i in range(1,10):
    root=Tk()
    root.geometry("1000x1000")
    f1=Frame(root)
    f1.pack()
    f2=Frame(root)
    f2.pack()

    lb=Label(f1,text=f'''It's 28th jan \nshivraj birthday!!!\nHAPPY BIRTHDAY TO YOU SHIVRAJ''',bg="gray",
             fg="black",padx="40",pady="20",font="arial 30 bold", borderwidth=10,relief=RAISED)
    lb.pack(anchor="ne",fill="x")
    pic=PhotoImage(file="3.png")
    lb=Label(f2,image=pic,bg="purple",
             fg="black",padx="40",pady="20",font="arial 20 bold", borderwidth=10,relief=RAISED)
    lb.pack(anchor="ne",fill="x")
    root.mainloop()
    time.sleep(0.4)
