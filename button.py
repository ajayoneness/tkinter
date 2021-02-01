from tkinter import *
obj=Tk()
def name():
    print ("ajay pandit")

def profilepic():
    root=Tk()
    root.geometry("0x0")
    root.title("ajay pandit")
    photo=PhotoImage(file="4.png")
    aj=Label(image=photo)
    aj.pack()
    root.mainloop()

def aboutus():
    print('''\n\n
The computer science engineer
expert on programming(c,c++,java,python,html,css,sql)
certified ethical hacker''')

def contactus():
    print('''\n\n
phonr no. : 0123456789
email : ajayoneness123@gmail.com
instagram.com/hacking_knowledge
www.codeajay.blogspot.com
fb.com/hackingknowledge''')
obj.geometry("500x900")
f1 =Frame(obj,bg="green",borderwidth=6,relief=RAISED)
f1.pack()
b1=Button(f1,text="contact us",font ="arial,20,bold",padx=10,pady=10,bg="gray",command=contactus)
b1.pack(side=RIGHT,anchor="nw")
b2=Button(f1,text="about us",font ="arial,10,bold",padx=10,pady=10,bg="gray",command=aboutus)
b2.pack(side=RIGHT,anchor="nw")
b3=Button(f1,text="profile pic",font ="arial,10,bold",padx=10,pady=10,bg="gray",command=profilepic)
b3.pack(side=RIGHT,anchor="nw")
b4=Button(f1,text="name",font ="arial,10,bold",padx=10,pady=10,bg="gray",command=name)
b4.pack(side=RIGHT,anchor="nw")
obj.mainloop()
