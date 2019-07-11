from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
root=Tk()


class employee:
    def __init__(self, first, last, pay): #u can call 'self' anything but it is convention to call it self
        self.first= first
        self.last= last
        self.pay = pay
        self.email= first + '.' + last + '@company.com'

def window1():
    label=Label(root, text="Customer Relationship Management ", bg="red").pack()
    button1=Button(root, text="login",command=loginpage).pack()




def loginpage():
    #top = Toplevel()
    pass


window1()

root.mainloop()