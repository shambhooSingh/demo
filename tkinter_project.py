import tkinter
from PIL import Image,ImageTk
import time
root=tkinter.Tk()
root.title("collage management system")
root.geometry("400x400")
root.configure(bg="light pink")
image=Image.open("D:\python\WhatsApp Image 2024-10-20 at 20.51.25_1b5dd35d.jpg")
photo=ImageTk.PhotoImage(image)
i1=tkinter.Label(root,image=photo)
i1.place(x=0,y=0)


l1=tkinter.Label(root,text="DR SHYAMA PRASHAD MUKHERJEE UNIVERSITY",bg="white",fg="black",font="algerian 40")
l1.pack()
l1=tkinter.Label(root,text="morabadi,ranchi-834004(jharkhand)",bg="white",fg="black",font="algerian 20")
l1.pack()


l2=tkinter.Label(root,text="Collage",bg="white",fg="black",font="arial 12")
l2.place(x=1420,y=10)

l2=tkinter.Label(root,text="management",bg="white",fg="black",font="arial 12")
l2.place(x=1420,y=30)

l2=tkinter.Label(root,text="system",bg="white",fg="black",font="arial 12")
l2.place(x=1420,y=50)


l2=tkinter.Label(root,text="REGISTRATION FOR STUDENT",bg="LIGHT PINK",fg="BLACK",font="arial 12")
l2.place(x=1120,y=150)
 

l2=tkinter.Label(root,text="ALL UNDER GRADUATE COURSES FOR",bg="LIGHT PINK",fg="black",font="arial 12")
l2.place(x=1120,y=170)


l3=tkinter.Label(root,text="ACADEMIC SEASON:23-27",bg="LIGHT PINK",fg="black",font="arial 12")
l3.place(x=1120,y=190)

l4=tkinter.Label(root,text="@2024 All rights reserved DR,SHYAMA PRASHAD MUKHERJEE UNIVERSITY",bg="BLACK",fg="WHITE",font="arial 12")
l4.place(x=350,y=710)

l1=tkinter.Label(root,text="=================================================================================================",bg="white",fg="black",font="algerian 20")
l1.pack()




def update():
    clock.config(text=time.strftime(" %d %B %y,%a-%I:%M:%S %p"))
    clock.after(1000,update)
clock = tkinter.Label(root, background = '#0ABFA2',fg = 'red', font = ('arial', 12,'italic','bold'))
clock.place(x=20,y=150)
update()




def reg():
    top=tkinter.Toplevel()
    top.title("Registratio process")
    top.geometry("300x300")
    top.configure(bg="light green")
    l1=tkinter.Label(top,text="DR SHYAMA PRASHAD MUKHERJEE UNIVERSITY",bg="black",fg="white",font="arial 40")
    l1.pack()
    l1=tkinter.Label(root,text="User Name")
    top.mainloop()

    


def radm():
    top=tkinter.Toplevel()
    top.title("Re-admission process")
    top.geometry("300x300")
    top.configure(bg="light gray")
    l1=tkinter.Label(top,text="DR SHYAMA PRASHAD MUKHERJEE UNIVERSITY",bg="black",fg="white",font="arial 40")
    l1.pack()
    top.mainloop()


def adm():
    top=tkinter.Toplevel()
    top.title("Admission process")
    top.geometry("300x300")
    top.configure(bg="light pink")
    l1=tkinter.Label(top,text="DR SHYAMA PRASHAD MUKHERJEE UNIVERSITY",bg="black",fg="white",font="arial 40")
    l1.pack()
    top.mainloop()


def rest():
    top=tkinter.Toplevel()
    top.title("view result")
    top.geometry("300x300")
    top.configure(bg="light red")
    l1=tkinter.Label(top,text="DR SHYAMA PRASHAD MUKHERJEE UNIVERSITY",bg="black",fg="whiTE",font="arial 40")
    l1.pack()
    top.mainloop()
    




b1=tkinter.Button(root,text="Registration process",bg="brown",fg="light gray",font="Arial 20",command=reg)
b1.place(x=70,y=300)

b1=tkinter.Button(root,text="re-admission process",bg="brown",fg="light gray",font="Arial 20",command=radm)
b1.place(x=70,y=500)

b1=tkinter.Button(root,text="admission process",bg="brown",fg="light gray",font="Arial 20",command=adm)
b1.place(x=800,y=300)

b1=tkinter.Button(root,text=" view result",bg="brown",fg="light gray",font="Arial 20",command=rest)
b1.place(x=800,y=500)

b2=tkinter.Button(root,text="Cancel",bg="brown",fg="white",font="arial 20",command=quit)
b2.place(x=1100,y=700)

root.mainloop()