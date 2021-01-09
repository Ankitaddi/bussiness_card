import os
import datetime
from tkinter import *
from PIL import ImageTk,Image
from time import sleep
strTime = datetime.datetime.now().strftime("%H:%M:%S  --%A:%B:%d:%Y")
#print(f" the time and date is {strTime}")


def got():
    #print(f"{namev.get(),addv.get(),numv.get(),amov.get()}\n")
    with open("ac.txt","a") as f:
        f.write(f"        {namev.get()}  ")
        f.write(f"Date And Time :{strTime}\n")
        f.write("Address :")
        f.write(f"{addv.get()}\n")
        f.write("Mo. number :")
        f.write(f"{numv.get()}\n")
        f.write("Ammount :")
        f.write(f"{amov.get()}\n\n")
        
        
def calc():
    e=ex.get()
    try:
        Label(text=".                                           .                                                          ",font="40").grid(row=8,column=10)
        f=eval(e)
        Label(text=f" {f}",font="30").grid(row=6,column=8)
    except:
        Label(text="Wrong input Only Numeric Value Accepted",font="30").grid(row=8,column=10) 
    
    
        
           
    
    
        
   
root=Tk()    
root.title("Bussiness")
root.iconbitmap('d.png')
img=ImageTk.PhotoImage(Image.open("home.png"))
Label(image=img).grid()
Label(root,text="Welcome to your Account Page",bg="orange",fg="green",relief=SUNKEN).grid(row=0,column=5,columnspan=3)
name=Label(root,text="Name",pady=15)
name.grid(row=1,column=1)
add=Label(root,text="Address",pady=15)
add.grid(row=2,column=1)
num=Label(text="Mo.Number",pady=15)
num.grid(row=3,column=1)
amo=Label(text="Ammount",pady=15)
amo.grid(row=4,column=1)
namev=StringVar()
addv=StringVar()
numv=StringVar()
amov=StringVar()
a=Entry(textvariable=namev).grid(row=1,column=2)
b=Entry(textvariable=addv).grid(row=2,column=2)
c=Entry(textvariable=numv).grid(row=3,column=2)
d=Entry(textvariable=amov).grid(row=4,column=2)
Button(text="Proceed",command=got,pady=6).grid(row=5,column=1)
cal=Label(text="Calculate your ammount")
cal.grid(row=1,column=8)
ex=StringVar()
w=Entry(root,textvariable=ex).grid(row=2,column=8)
Button(text="Calculate",command=calc,pady=6).grid(row=3,column=8)
w=Entry(root,textvariable=ex).grid(row=2,column=8)

          


root.mainloop()
