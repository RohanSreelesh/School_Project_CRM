from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import pickle as p

mysql_password=''

def import_userdict():
    global userdict
    f=open('users','rb')
    userdict=p.load(f)
    f.close()
import_userdict()

def add():
    window = Tk()
    window.geometry("300x300")
    window.configure(bg='pink')
    lblTitle = Label(window, text="ADD CUSTOMER",font = "Arial,12",bg = "Yellow")
    lblTitle.pack()
    lblsales_id = Label(window, text='Enter unique salesman id')

    lblsales_id.place(x=30, y=20)

    entrysales_id = Entry(window)

    entrysales_id.place(x=160, y=20)
    lblcust_id = Label(window, text="Enter Customer Id")
    lblcust_id.place(x = 30,y = 50)


    entrycust_id = Entry(window)
    entrycust_id.place(x = 160, y = 50)

    lblname = Label(window, text="Enter Customer Name")
    lblname.place(x = 30,y = 80)

    entryname = Entry(window)
    entryname.place(x = 160,y = 80)

    lblph_no = Label(window, text="Enter Customer Phone")
    lblph_no.place(x = 30,y = 110)

    entryph_no = Entry(window)
    entryph_no.place(x = 160,y = 110)

    lblemail = Label(window, text="Enter Customer Email")
    lblemail.place(x = 30,y = 140)

    entryemail = Entry(window)
    entryemail.place(x = 160,y = 140)

    lblgender = Label(window, text="Enter Customer Gender")
    lblgender.place(x = 30,y = 170)

    entrygender = Entry(window)
    entrygender.place(x = 160,y = 170)

    lbladdress = Label(window, text="Enter Customer Address")
    lbladdress.place(x = 30,y = 200)

    entryaddress = Entry(window)
    entryaddress.place(x = 160,y = 200)

    lblpayment_mode = Label(window, text="Enter Value")
    lblpayment_mode.place(x = 30,y = 230)

    entrypayment_mode = Entry(window)
    entrypayment_mode.place(x = 160,y = 230)
    
    lblpayment = Label(window, text='Enter value')
    lblpayment.place(x=30,y=260)
    
    entrypayment = Entry(window)
    entrypayment.place(x = 160,y = 260)    

    def Save(): #for orders
        sales_id= entrysales_id.get()
        cust_id = entrycust_id.get()
        name = entryname.get()
        ph_no = entryph_no.get()
        email = entryemail.get()
        gender = entrygender.get()
        address = entryaddress.get()
        mode=entrypayment_mode.get()
        value = entrypayment.get()
        
        

        print(sales_id,cust_id, name, ph_no, email, gender, address, mode, value)
        sql = "insert into customer values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(sales_id,cust_id, name, ph_no,
                                                                                             email, gender, address, mode,
                                                                                             value)

        sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",auth_plugin='mysql_native_password')


        cursor = sql_connection.cursor()
        cursor.execute(sql)

        sql_connection.commit()

        print(name, " Saved in DataBase")


    Button(window, text="Save", command=Save).pack(side=BOTTOM)
    window.mainloop()

def update():

    def update_name():
        window1 = Tk()
        window1.geometry("200x200")
        window1.configure(bg='powderblue')
        lblTitle = Label(window1, text="Update Name",font = "Arial,12",bg = "Yellow")
        lblTitle.pack()

        lblname = Label(window1, text="Enter Customer New Name")
        lblname.pack()
        entryname = Entry(window1)
        entryname.pack()

        lblemail = Label(window1, text="Enter Customer Email")
        lblemail.pack()
        entryemail = Entry(window1)
        entryemail.pack()
        def update1():
         name = entryname.get()
         email = entryemail.get()

         print(name, email)
         sql = "update customer set name='{}' where email='{}'".format(name, email)

         sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",auth_plugin='mysql_native_password')

         cursor = sql_connection.cursor()
         cursor.execute(sql)

         sql_connection.commit()

         print(name, " Update in DataBase")

        Button(window1, text="Update Name", command=update1).pack(side=BOTTOM)
        window1.mainloop()

    def update_phone():
        window2 = Tk()
        window2.geometry("200x200")
        window2.configure(bg='powderblue')
        lblTitle = Label(window2, text="Update Phone",font = "Arial,12",bg = "Yellow")
        lblTitle.pack()

        lblph_no = Label(window2, text="Enter Customer New Phone")
        lblph_no.pack()
        entryph_no = Entry(window2)
        entryph_no.pack()

        lblname = Label(window2, text="Enter Customer Name")
        lblname.pack()
        entryname = Entry(window2)
        entryname.pack()
        def update2():
         ph_no = entryph_no.get()
         name = entryname.get()

         print(ph_no, name)
         sql = "update customer set ph_no='{}' where name='{}'".format(ph_no, name)

         sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project", auth_plugin='mysql_native_password')

         cursor = sql_connection.cursor()
         cursor.execute(sql)

         sql_connection.commit()

         print(ph_no, " Update in DataBase")

        Button(window2, text="Update Phone", command=update2).pack(side=BOTTOM)
        window2.mainloop()

    def update_email():
        window3 = Tk()
        window3.geometry("200x200")
        window3.configure(bg='powderblue')
        lblTitle = Label(window3, text="Update Email",font = "Arial,12",bg = "Yellow")
        lblTitle.pack()

        lblemail = Label(window3, text="Enter Customer New Email")
        lblemail.pack()
        entryemail = Entry(window3)
        entryemail.pack()

        lblname = Label(window3, text="Enter Customer Name")
        lblname.pack()
        entryname = Entry(window3)
        entryname.pack()

        def update3():
            email = entryemail.get()
            name = entryname.get()

            print(email, name)
            sql = "update customer set email='{}' where name='{}'".format(email, name)

            sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(email, " Update in DataBase")

        Button(window3, text="Update Email", command=update3).pack(side=BOTTOM)
        window3.mainloop()

    def update_address():
        window4 = Tk()
        window4.geometry("200x200")
        window4.configure(bg='powderblue')
        lblTitle = Label(window4, text="Update Address",font = "Arial,12",bg = "Yellow")
        lblTitle.pack()

        lbladdress = Label(window4, text="Enter Customer New Address")
        lbladdress.pack()
        entryaddress = Entry(window4)
        entryaddress.pack()

        lblname = Label(window4, text="Enter Customer Name")
        lblname.pack()
        entryname = Entry(window4)
        entryname.pack()

        def update4():
            address = entryaddress.get()
            name = entryname.get()

            print(address, name)
            sql = "update customer set address='{}' where name='{}'".format(address, name)

            sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",
                          auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(address, " Update in DataBase")

        Button(window4, text="Update Address", command=update4).pack(side=BOTTOM)
        window4.mainloop()

    def update_paymentmode():
        window5 = Tk()
        window5.geometry("200x200")
        window5.configure(bg='powderblue')
        lblTitle = Label(window5, text="Update Payment Mode",font = "Arial,12",bg = "Yellow")
        lblTitle.pack()

        lblpayment_mode = Label(window5, text="Enter Updated Payment Mode")
        lblpayment_mode.pack()
        entrypayment_mode = Entry(window5)
        entrypayment_mode.pack()

        lblname = Label(window5, text="Enter Customer Name")
        lblname.pack()
        entryname = Entry(window5)
        entryname.pack()

        def update5():
            payment_mode = entrypayment_mode.get()
            name = entryname.get()

            print(payment_mode, name)
            sql = "update customer set payment_mode='{}' where name='{}'".format(payment_mode, name)

            sql_connection= mysql.connect(user="root", password=mysql_password, host="localhost", database="project",
                          auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(payment_mode, " Update in DataBase")

        Button(window5, text="Update Payment Mode", command=update5).pack(side=BOTTOM)
        window5.mainloop()

    def update__():
      win1 = Tk()
      frame1 = Frame(win1)
      frame1.pack()
      b1 = Button(frame1, text="Update Customer Name", command=update_name)
      b2 = Button(frame1, text="Update Customer Phone", command=update_phone)
      b3 = Button(frame1, text="Update Customer Email", command=update_email)
      b4 = Button(frame1, text="Update Customer Address", command=update_address)
      b5 = Button(frame1, text="Update Payment Mode", command=update_paymentmode)

      b1.pack()
      b2.pack()
      b3.pack()
      b4.pack()
      b5.pack()

    win1 = update__()
    win1.mainloop()

def delete():
    root = Tk()

    lblTitle = Label(root, text="Enter Name",font = "Arial,16",bg = "Yellow")
    lblTitle.pack()

    lblname = Label(root, text="Enter Customer Name")
    lblname.pack()

    entryname = Entry(root)
    entryname.pack()

    def DeleteIt():
      name = entryname.get()
      print(name)

      sql = "delete from customer where name = '{}'".format(name)
      sql_connection= mysql.connect(user="root", password=mysql_password, host="localhost", database="project",
                    auth_plugin='mysql_native_password')

      cursor = sql_connection.cursor()
      cursor.execute(sql)
      sql_connection.commit()
      print(name, " Delete from DataBase")

    Button(root, text="Delete", command=DeleteIt).pack(side=BOTTOM)
    root.mainloop()

def view():

    root2 = Tk()

    lblname = Label(root2, text="Enter Customer Name")
    lblname.pack()

    entryname = Entry(root2)
    entryname.pack()

    def ShowIt():
        name = entryname.get()
        print(name)

        sql = "select * from customer where name = '{}'".format(name)
        sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",
                      auth_plugin='mysql_native_password')

        cursor = sql_connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    Button(root2, text="Show", command=ShowIt).pack(side=BOTTOM)
    root2.mainloop()

def view_all():
    sql = "select * from customer"

    sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",
                  auth_plugin='mysql_native_password')

    cursor = sql_connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

def view_sales():
    root2 = Tk()

    lblsales_id = Label(root2, text="Enter Your Sales ID")
    lblsales_id.pack()

    entrysales_id = Entry(root2)
    entrysales_id.pack()
    def ShowIt():
        sales_id = entrysales_id.get()
        print(sales_id)

        sql = "select payment from customer where sales_id = '{}'".format(sales_id)
        sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",auth_plugin='mysql_native_password')

        cursor = sql_connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
        total=0
        for i in rows:
            total+=i
        print('Gross Sales:',total)

    Button(root2, text="Show", command=ShowIt).pack(side=BOTTOM)
    root2.mainloop()

def customer_all():
    win = Tk()
    win.geometry("400x400")
    win.configure(bg='bisque')
    lblTitle = Label(win, text="SELECT YOUR CHOICE!!!!",font = "Arial,16",bg = "Yellow")
    lblTitle.pack()
    b1 = Button(win, text=" Add Customer", command=add,fg = "red")
    b2 = Button(win, text="Update Customer", command=update,fg = "purple")
    b3 = Button(win, text="Delete Customer", command=delete,fg = "orange")
    b4 = Button(win, text="View Customer", command=view,fg = "green")
    b5 = Button(win, text="View All Customers", command=view_all,fg = "blue")
    b6 = Button(win, text="View sales", command=view_sales, fg='IndianRed4')
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    b6.pack()
    win.mainloop()

def login():
    global loginwindow,usernameentry,passwordentry
    # this label notifies progress find a way so that it does not stack
    Label(loginwindow, text="loading", font="Arial,12", bg="Yellow").pack()

    user = usernameentry.get()

    password = passwordentry.get()

    userlist = list(userdict.keys())

    if user == userlist[0]:

        if userdict[user] == password:

            messagebox.showinfo("SUCCESS", "WELCOME BACK BOSS")

            loginwindow.destroy()

            #customer_all()
            manager_page()

        else:

            Label(loginwindow, text="wrong password", font="Arial,12", bg="Yellow").pack()

    elif user in userlist:

        if userdict[user] == password:

            messagebox.showinfo("SUCCESS", "WELCOME BACK " + user)

            loginwindow.destroy()

            #customer_all()
            selection()
        else:

            Label(loginwindow, text="wrong password", font="Arial,12", bg="Yellow").pack()
    else:

        Label(loginwindow, text="wrong username", font="Arial,12", bg="Yellow").pack()

    loginwindow.mainloop()
# login page starts here label and entry ko side by side kar de
def login_front():
    global loginwindow, usernameentry, passwordentry
    loginwindow = Tk()

    loginwindow.geometry("300x170")

    loginwindow.configure(bg='bisque')

    lbluser = Label(loginwindow, text="ENTER USERNAME", font="Arial,12", bg="Yellow")

    lbluser.pack()

    usernameentry = Entry(loginwindow)

    usernameentry.pack()

    Label(loginwindow, text="ENTER PASSWORD", font="Arial,12", bg="Yellow").pack()

    passwordentry = Entry(loginwindow)

    passwordentry.pack()

    loginbutton = Button(loginwindow, text="LOGIN", command=login, fg="blue")

    loginbutton.pack()

    loginwindow.mainloop()

def selection_leads():
    win = Tk()
    win.geometry("300x170")
    win.configure(bg='bisque')
    lblTitle = Label(win, text="SELECT YOUR CHOICE!!!!", font="Arial,16", bg="Yellow")
    lblTitle.pack()
    b1 = Button(win, text="Add Leads", command=add_leads, fg="red")
    b3 = Button(win, text="Delete Leads", command=delete_leads, fg="orange")
    b4 = Button(win, text="View Lead", command=view_leads, fg="green")
    b5 = Button(win, text="View All Leads", command=view_all_leads, fg="blue")
    b1.pack()
    b3.pack()
    b4.pack()
    b5.pack()

def add_leads():
    window= Tk()
    window.geometry('300x170')
    window.configure(bg='pink')
    lb_title= Label(window,text='Name',font = "Arial,12",bg = "Yellow")
    lb_title.pack()

    lbname = Label(window, text='Name')

    lbname.place(x=30, y=20)

    entry_lbname = Entry(window)

    entry_lbname.place(x=160, y=20)
    lblcategory = Label(window, text="Category")
    lblcategory.place(x=30, y=50)

    entry_lblcategory = Entry(window)
    entry_lblcategory.place(x=160, y=50)

    lblph_no = Label(window, text="Phone number")
    lblph_no.place(x=30, y=80)

    entry_lblph_no = Entry(window)
    entry_lblph_no.place(x=160, y=80)

    lbl_meet = Label(window, text="Next meeting")#put date picker here
    lbl_meet.place(x=30, y=110)

    entry_lbl_meet = Entry(window)
    entry_lbl_meet.place(x=160, y=110)
    def Save(): #for orders
        name= entry_lbname.get()
        category = entry_lblcategory.get()
        phone = entry_lblph_no.get()
        meet = entry_lbl_meet.get()


        print(name,category,phone,meet)
        sql = "insert into leads values('{}', '{}', '{}', '{}')".format(name,category,phone,meet)


        sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",auth_plugin='mysql_native_password')


        cursor = sql_connection.cursor()
        cursor.execute(sql)

        sql_connection.commit()

        print(name, " Saved in DataBase")


    Button(window, text="Save", command=Save).pack(side=BOTTOM)
    window.mainloop()

def delete_leads():
    root = Tk()

    lblTitle = Label(root, text="Enter Name",font = "Arial,16",bg = "Yellow")
    lblTitle.pack()

    lblname = Label(root, text="Enter Lead Name")
    lblname.pack()

    entryname = Entry(root)
    entryname.pack()

    def DeleteIt_leads():
      name = entryname.get()
      print(name)

      sql = "delete from leads where name = '{}'".format(name)
      sql_connection= mysql.connect(user="root", password=mysql_password, host="localhost", database="project",
                    auth_plugin='mysql_native_password')

      cursor = sql_connection.cursor()
      cursor.execute(sql)
      sql_connection.commit()
      print(name, " Delete from DataBase")

    Button(root, text="Delete", command=DeleteIt_leads).pack(side=BOTTOM)
    root.mainloop()

def view_leads():

    root2 = Tk()

    lblname = Label(root2, text="Enter Customer Name")
    lblname.pack()

    entryname = Entry(root2)
    entryname.pack()

    def ShowIt():
        name = entryname.get()
        print(name)

        sql = "select * from leads where name = '{}'".format(name)
        sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",
                      auth_plugin='mysql_native_password')

        cursor = sql_connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3])

    Button(root2, text="Show", command=ShowIt).pack(side=BOTTOM)
    root2.mainloop()

def view_all_leads():
    sql = "select * from leads"

    sql_connection = mysql.connect(user="root", password=mysql_password, host="localhost", database="project",
                  auth_plugin='mysql_native_password')

    cursor = sql_connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3])


def add_salesman():  
    import pickle as p
    key=input('Enter the employee name:')
    password=input('Enter password:')
    f=open('users','rb+')
    userdict=p.load(f)
    if key in userdict.keys():
        return 'employee already exists'
    else:
        userdict[key]=password
        f.seek(0)
        
        p.dump(userdict,f)
        return 'EMPLOYEE ADDED:',userdict
        
        
        
    f.flush()
    f.close()
def manager_page():
    win = Tk()
    win.geometry("400x400")
    win.configure(bg='bisque')
    lblTitle = Label(win, text="SELECT YOUR CHOICE!!!!",font = "Arial,16",bg = "Yellow")
    lblTitle.pack()
    b1 = Button(win, text=" Add Salesman", command=add_salesman,fg = "red")
    b2 = Button(win, text="Update Salesman", command=update,fg = "purple")
    b3 = Button(win, text="View all sales", command=delete,fg = "orange")
    '''b4 = Button(win, text="View Customer", command=view,fg = "green")
    b5 = Button(win, text="View All Customers", command=view_all,fg = "blue")
    b6 = Button(win, text="View sales", command=view_sales, fg='IndianRed4')'''
    b1.pack()
    b2.pack()
    b3.pack()
    '''b4.pack()
    b5.pack()
    b6.pack()'''
    win.mainloop()
#both are same as customer only small changes
def selection():
    win = Tk()
    win.geometry("300x170")
    win.configure(bg='bisque')
    lblTitle = Label(win, text="SELECT YOUR CHOICE!!!!", font="Arial,16", bg="Yellow")
    lblTitle.pack()
    b1 = Button(win, text=" Leads", command=selection_leads, fg="red")
    b2 = Button(win, text="Orders", command=customer_all, fg="purple")
    b1.pack()
    b2.pack()

    win.mainloop()







login_front()
'''
def add_salesman():  
    import pickle as p
    key=input('Enter the employee name:')
    password=input('Enter password:')
    f=open('users','rb+')
    userdict=p.load(f)
    if key in userdict.keys():
        print('employee already exists')
    else:
        userdict[key]=password
        f.seek(0)
        
        p.dump(userdict,f)
        
        
    f.flush()
    f.close()

def update_salesman():
    usernameorpass=input('enter 0 to change user or 1 for password')
    f=open('users','rb+')
    userdict=p.load(f)
    
    
def import_userdict():
    global userdict
    f=open('users','rb')
    userdict=p.load(f)
    f.close()
    
def createuserfile():
    userdict={'admin':'1234'}
    f=open('users','wb')
    userdict=p.dump(userdict,f)
    f.flush()
    f.close()
createuserfile()
import_userdict()
print(userdict)    
    


def manager_page():
    win = Tk()
    win.geometry("400x400")
    win.configure(bg='bisque')
    lblTitle = Label(win, text="SELECT YOUR CHOICE!!!!",font = "Arial,16",bg = "Yellow")
    lblTitle.pack()
    b1 = Button(win, text=" Add Salesman", command=add_salesman,fg = "red")
    b2 = Button(win, text="Update Salesman", command=update,fg = "purple")
    b3 = Button(win, text="View all sales", command=delete,fg = "orange")
    b4 = Button(win, text="View Customer", command=view,fg = "green")
    b5 = Button(win, text="View All Customers", command=view_all,fg = "blue")
    b6 = Button(win, text="View sales", command=view_sales, fg='IndianRed4')
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    b6.pack()
    win.mainloop()
    
manager_page()
'''
