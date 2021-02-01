from tkinter import *
#BORDER STYLE(relief)= SUNKEN, RAISED, GROOVE, RIDGE 
root=Tk()
root.geometry("600x300")
photo=PhotoImage(file="1.png")

lb=Label(text='''hi i am Ajay pandit \nfrom malangwa sarlahi nepal\ncomputer science engineer\n thanku for visiting..... ''',bg="gray",
         fg="black",padx="40",pady="20",font="arial 20 bold", borderwidth=10,relief=RAISED) 
lb.pack()
root.mainloop()
