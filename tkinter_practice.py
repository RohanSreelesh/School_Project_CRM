#%% tutorial 1,2,3 LABELS, FRAMES, FITTING WIDGETS
from tkinter import *
root=Tk()
frame=Frame(root)
label=Label(root, text="bht easy hai!!", bg="red")
label2=Label(root, text='TEst', bg='yellow')
button1=Button(frame, text="CLICK ME!!")
button2=Button(frame, text="Click me instead!!")
bframe=Frame(root)
button3=Button(bframe, text="Click moi instead!!")
bframe.pack(side=BOTTOM)
button2.pack(side=RIGHT)
button1.pack(side=LEFT)
button3.pack()
label.pack(fill=X)
label2.pack(side=LEFT,fill=Y)
frame.pack()
root.mainloop()
#%% tutorial4 GRIDLAYOUT
from tkinter import *
root=Tk()
name=Label(root, text="name:")
password=Label(root, text="password:")
entry1=Entry(root)
entry2=Entry(root)
name.grid(row=0, column=0, sticky= E)
entry1.grid(row=0, column=1)
password.grid(row=1, column=0)
entry2.grid(row=1, column=1)
c=Checkbutton(root, text="keep me logged in")
c.grid(columnspan=2)
root.mainloop()
#%% tutorial 5 BINDING FUNCTIONS TO BUTTONS
from tkinter import *
root = Tk()
'''method 1'''
def call_me():
    print('IM CALLED')
button= Button(root, text="click me", command=call_me)
'''method 2'''
def call_me2(event):
    print('this is method 2')
button2= Button(root, text="click me")
button2.bind("<Button-1>", call_me2)
button.pack()
button2.pack()
root.mainloop()
#%% tutorial 6 MOUSE CLICK EVENTS
from tkinter import *
root= Tk()
def rightClick(event):
    print('Right click')
def leftClick(event):
    print('left click')
def middleClick(event):
    print('mouse click')
frame= Frame(root, width=300, height=300)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()
root.mainloop()
#%% tutorial 7 SET WIDTH AND HEIGHT AND MESSAGE BOX , ASKING QUESTIONS
from tkinter import *
from tkinter import messagebox
root= Tk()


def call_me():
    messagebox.showinfo("SUCCESS", "INSTALLATION COMPLETE")#showinfo is used for icon
def call_me2():
    answer=messagebox.askquestion("exit","Do you really want to exit?")
    print(answer)
    if answer=='yes':
        root.quit()
def callme3():
    answer2=messagebox.askyesnocancel("exit","Do you really want to exit?")
    print(answer2)
    if answer2==True:
        root.quit()
a=Button(root, text="messagebox", command=call_me)
a.pack()
c=Button(root, text="exit1", command=call_me2)
c.pack()
b=Button(root, text="exit2", command=callme3)
b.pack()


root.geometry("600x300+120+120") #syntax= width*height+dist_from_x-axis_of_screen+dist_from_y-axis_of_screen
root.mainloop()
#%% TUTORIAL 8 WORKING WITH CLASSES
from tkinter import *

class myButtons:
    def __init__(self,master):
        self.printButton = Button(master, text="print", command=self.printMessage)
        self.printButton.pack(side=LEFT)
        self.quitButton= Button(master, text='QUIT', command=master.quit)
        self.quitButton.pack(side=LEFT)
    def printMessage(self):
        print("printing message")
root=Tk()
b=myButtons(root)
root.mainloop()
#%% TUTORIAL 9 DROP DOWN MENUS AND SUB-MENUS
from tkinter import *

def do_nothing():
    print("Ok ok i wont")


root=Tk()
main_menu=Menu(root, tearoff=0)
root.config(menu=main_menu)

fileMenu=Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="file" , menu=fileMenu)

editMenu=Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="edit" , menu=fileMenu)

fileMenu.add_command(label="new project", command=do_nothing)
fileMenu.add_command(label="new scratch file", command=do_nothing)
fileMenu.add_separator()
fileMenu.add_command(label="open", command=do_nothing)
save_menu=Menu(fileMenu,tearoff=0)
save_menu.add_command(label="save as new", command=do_nothing)
save_menu.add_command(label="save now" , command = do_nothing)
fileMenu.add_cascade(label="save", menu=save_menu)# SUB MENU



root.mainloop()
#%% TUTORIAL 10 CANVAS 
from tkinter import *

root=Tk()
canvas=Canvas(root, width=900, height=900, bg='red')
canvas.pack()

#CREATING LINES
line = canvas.create_line(0,0,200,100) #(x1,y1,x2,y2)
blueline = canvas.create_line(200,100,0,200, fill='blue')

#CREATING ARCS
arc=canvas.create_arc(100,100,200,200)
arc_extent=canvas.create_arc(850,750,200,200, extent=120) #extent=angle(if u want to change it from 90)

'''#CREATING IMAGES (.png or .gif)
photo = PhotoImage(file='.png image file here') #python doesnt take '\' so use '\\
photo = PhotoImage(file='C:\\Users\\Tishabh\\Desktop\\198955.png')
canvas.create_image(0,0, image=photo, anchor=NW) #anchor is to show which part of the image should start from the specified coordinates'''

#CREATING RECTANGLES
rect= canvas.create_rectangle(400,400,200,250, fill='blue',outline='red')

#CREATING OVALS CAN BE USED TO MAKE CIRCLES...BE SMART
oval=canvas.create_oval(400,400,200,250)
circle= canvas.create_oval(900,900,0,0, outline='white')
#CREATING POLYGONS
points=[250,110,480,200,280,280,250,110] #first point should be given to make a closed figure
canvas.create_polygon(points, fill='green' , outline='yellow')
root.geometry("1200x720+120+120")
root.mainloop()

#%% TUTORIAL 11 GEOMETRY MANAGER (PACK,GRID, PLACE) we are done with pack and grid
from tkinter import *
root=Tk()

label1=Label(root, text='label1')
label2=Label(root, text='label2')

label1.pack(side=LEFT) #THESE ARE THE OLD METHODS....WE DONT DO THAT HERE
label2.place(x=120,y=120)# unit of co-ods is pixels

root.geometry("1200x720+120+120")
root.mainloop()
#%%TUTORIAL 12 TAKING INPUTS(THE REAL SHIT)
from tkinter import *
root=Tk()
'''METHOD-1'''
def do_nothing():
    s=entry.get()
    print(entry.get())
    print(s)# we can use this for login

entry=Entry(root)
entry.pack()

button=Button(root,text='click' ,command=do_nothing)
button.pack()

'''METHOD-2'''
def click_me():
    s1=s.get()
    print(s1)
s=StringVar()
entry2=Entry(root, textvariable=s)
s.set("welcome")#IDHAR HI INPUT STATEMENT DE DENGE
s.get()
entry2.pack()
button2=Button(root,text='click' ,command=click_me)
button2.pack()
root.geometry("1200x720+120+120")
root.mainloop()
#%% TUTORIAL 13 CHECKBUTTON AND RADIOBUTTON
from tkinter import *
root=Tk()

def click_me():
    print(f.get())

f=StringVar()
c= Checkbutton(root, text="item 1", variable=f, offvalue="unchecked", onvalue="checked")
c.pack()

button= Button(root, text='click me', command=click_me)
button.pack()

#RADIOBUTTONS

def check():
    if i.get()==1:
        print('YOU ARE MALE')
    elif i.get()==2:
        print('YOU ARE FEMALE')

i=IntVar()
r1= Radiobutton(root, text='male', value=1, variable=i)
r2= Radiobutton(root, text='female', value=2, variable=i)
r1.pack()
r2.pack()

button2=Button(root, text='check', command=check)
button2.pack()

root.geometry("1200x720+120+120")
root.mainloop()
#%% LISTBOX
from tkinter import *
root=Tk()

def print_me():
    clicked_items=l.curselection()# returns tuple of indexes
    for item in clicked_items:
        print(item)#returns indexes only
        print(l.get(item))#syntax (name.get(index))
    
def delete():
        clicked_items=l.curselection()# returns tuple of indexes
        for item in clicked_items:
            print(l.delete(item))#print will print none
    
    
l=Listbox(root, width=30, height=15, selectmode=MULTIPLE)#width = number of chars in a line, height refers to number of lines, default width=20 and default height 10, selectmode default is BROWSE...other options are 'SINGLE','MULTIPLE','EXTENDED'
l.insert(1,"C++")
l.insert(2,"C#")
l.insert(3,"JAVA")
l.insert(4,"PYTHON")
l.insert(5,"UNITY")
l.pack()

button=Button(root, text="print", command=print_me)
button.pack()
del_but=Button(root, text='delete value' ,command=delete).pack()


root.geometry("1200x720+120+120")
root.mainloop()
#%% COMBOBOX
from tkinter import *
from tkinter.ttk import Combobox as cb
root=Tk()

def print_me():
    value=combo2.get()
    print(value)
v=['c++','c#','python']

combo=cb(root, values=v, width=15,height=20)
combo.set('languages')
combo.pack()
#EXAMPLE
date=list(range(1,32))
combo2=cb(root, values=date, width=15,height=20)
combo2.set('select date')
combo2.pack()

button=Button(root, text='print' ,command=print_me).pack()
root.geometry("1200x720+120+120")
root.mainloop()
#%% FONTS
from tkinter import *
from tkinter.font import Font as f
from tkinter import font
root=Tk()

myfont=f(family='Yu Gothic Light',size=16, weight='bold', slant='italic', underline=1, overstrike=1)
label=Label(root, text='HYPE INTENSIFIES', font=myfont).pack()

fonts=list(font.families())
for i in fonts:
    print(i)

root.geometry("1200x720+120+120")
root.mainloop()
#%% TEXT!!!!!!!!! 
from tkinter import *
root=Tk()



def print_me():
    value=text.get(1.0, END)# kind of like seek range...1.0=first char to end char....1.0 = LINE.CHAR SO 1.0 MEANS 1ST LINE 0TH CHAR WHICH IS KIND OF LIKE INDEXING IN A LIST
    print(value)
def selected_text():
    result=text.selection_get()
    print(result)    
def search():
    result=text.selection_get()
    pos=text.search(result, 1.0, stopindex=END)
    print(pos)
    
text=Text(root, width=20,height=10, wrap=WORD, padx=10, pady=5,bd=6, selectbackground='green', selectforeground='black')

text.pack()
text.insert(INSERT, 'hello i am RISHABH')

button=Button(root, text='print all text' ,command=print_me).pack()
button2=Button(root, text='print selected text' ,command=selected_text).pack()
button3=Button(root, text='show position' ,command=search).pack()



root.geometry("1200x720+120+120")
root.mainloop()
#%% SCROLLBAR
from tkinter import *
root=Tk()

frame=Frame(root)
scroll= Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

listbox= Listbox(frame, yscrollcommand=scroll.set)

for i in range(1,100):
    listbox.insert(END, "list" + str(i))
listbox.pack(side=LEFT)
scroll.config(command=listbox.yview)
frame.pack()
root.geometry("1200x720+120+120")
root.mainloop()
#%%% BASIC SEARCH APP
from tkinter import *
import wikipedia

def get_me():
    entry_value=entry.get()
    text.delete(1.0,END)
    try:
        answer_value=wikipedia.summary(entry_value)
        text.insert(INSERT, answer_value)
    except:
        text.insert(INSERT, "please check your input or internet connection")
root=Tk()


topframe=Frame(root)
entry=Entry(topframe)
entry.pack()
button=Button(topframe, text='search', command=get_me).pack()
topframe.pack(side=TOP)




bottomframe=Frame(root)
scroll= Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
text=Text(bottomframe, yscrollcommand=scroll.set,wrap=WORD)

scroll.config(command=text.yview)
text.pack()
bottomframe.pack()




root.mainloop()
#%%  INPUTS THROUGH POPUP WINDOW
from tkinter import *
from tkinter import simpledialog
root=Tk()

def get_me():
    name=simpledialog.askstring("INPUT STRING", "please enter your name")#title, prompt
    print(name)


button=Button(root, text='popup', command=get_me).pack()


root.mainloop()
#%% SLIDER
from tkinter import *
root=Tk()

s = Scale(root, from_=0, to = 100, orient=HORIZONTAL, length=200, width=20, sliderlength=50)
'''s.set(100)'''# sets default start value
s.pack(side=LEFT)
print(s.get())# YOU CAN MAKE A FUNCTION TO GET THE SLIDER VALUE WHEN A BUTTON IS PRESSED




root.mainloop()
#%% MULTIPLE WINDOWS
from tkinter import *
root=Tk()

def open_window():
    top = Toplevel()
    top.title("top window")
    top.geometry("1200x720+120+120")
    button1=Button(top, text='close', command=top.destroy).pack()


button=Button(root,text='open window', command=open_window).pack()


root.geometry("1200x720+120+120")
root.mainloop()
#%% SPINBOX
from tkinter import *
root=Tk()

def get():
    print(spin1.get())
button=Button(root, text='print', command=get).pack()


spin1=Spinbox(root, from_=1, to = 5)
spin1.pack()


root.geometry("1200x720+120+120")
root.mainloop()
#%%
from tkinter import *
root=Tk()

frame= LabelFrame(root, text='INPUT',padx=5, pady=5)
entry=Entry(frame).pack()
frame.pack()


root.geometry("1200x720+120+120")
root.mainloop()
#%%
from tkinter import *
from tkinter import filedialog 
root=Tk()

def open_file():
       result =  filedialog.askopenfile(initialdir="/", title="select file", filetypes=(("text files", ".txt"), ("all files", "*.*")))
       print(result)
       for c in result:
           print(c)

button=Button(root,text='open file' , command=open_file).pack()



root.geometry("1200x720+120+120")
root.mainloop()
