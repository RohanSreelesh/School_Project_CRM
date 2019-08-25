from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox as cb
import mysql.connector as mysql
import pickle as p
import matplotlib.pyplot as plt
import numpy as np
import random
import time

mysql_password = 'Rohan2002'
hostname = 'localhost'
salesidcount=3
f3 = open('count_check','w+')
f3.write(str(salesidcount))
f3.close()
cust_ids_customer = []
cust_ids_leads = []
total_sales_list_final = []
id_list_final = []

def createuserfile():
    userdict = {'admin': '1234', 'avig': '1234', 'rohan': '1234', 'rishabh': '1234'}
    f = open('users', 'wb+')
    p.dump(userdict, f)
    f.flush()
    f.close()
def createsalesidfile():
    sales_ids = {'admin': 'Null', 'avig': '2', 'rohan': '1', 'rishabh': '3'}
    f = open('salesids', 'wb+')
    p.dump(sales_ids, f)
    f.flush()
    f.close()



def import_userdict():
    global userdict
    f = open('users', 'rb+')
    userdict = p.load(f)
    f.close()
def import_salesids():
    global sales_ids_dict
    f = open('salesids','rb+')
    sales_ids_dict = p.load(f)
    f.close()




sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                               port=3306, auth_plugin='mysql_native_password')

cursor_main = sql_connection.cursor()

cursor_main.execute('create database if not exists project')

cursor_main.execute('use project;')

cursor_main.execute(
    'create table if not exists customer (sales_id varchar(10),cust_id varchar(10) unique,name varchar(100) '
    ',phone_no varchar(10),email varchar(100),gender varchar(6),address varchar(500),mode varchar('
    '10),value varchar(10));')

cursor_main.execute(
    'create table if not exists leads (cust_id varchar(30) unique,name varchar(50),cust_type varchar(50),'
    'phone_no varchar(10) , '
    'next_meeting varchar(30));')

cursor_main.execute('select cust_id from customer;')
rows=cursor_main.fetchall()
for i in rows:
    cust_ids_customer.append(i[0])

cursor_main.execute('select cust_id from leads;')
rows=cursor_main.fetchall()
for i in rows:
    cust_ids_leads.append(i[0])

def delete_Check():
    messagebox.askyesno('DELETE', 'DO YOU REALLY WANT TO DELETE')


def add():
    global rando_id, cust_ids_customer
    window = Toplevel()
    window.geometry("330x300")
    window.configure(bg='pink')

    lblTitle = Label(window, text="ADD CUSTOMER", font="Arial,12", bg="Yellow")
    lblTitle.pack()

    lblsales_id = Label(window, text='Unique salesman id')
    lblsales_id.place(x=10, y=20)

    lblsales_id = Label(window, text=sales_id_user)
    lblsales_id.place(x=160, y=20)

    lblcust_id = Label(window, text="Customer Id")
    lblcust_id.place(x=10, y=50)

    rando_id = str(random.randint(0, 99999))
    cust_ids_customer.append(rando_id)

    lblcust_id = Label(window, text=rando_id)
    lblcust_id.place(x=160, y=50)

    lblname = Label(window, text="Enter Customer Name")
    lblname.place(x=10, y=80)

    entryname = Entry(window)
    entryname.place(x=160, y=80)

    lblph_no = Label(window, text="Enter Customer Phone")
    lblph_no.place(x=10, y=110)

    entryph_no = Entry(window)
    entryph_no.place(x=160, y=110)

    lblemail = Label(window, text="Enter Customer Email")
    lblemail.place(x=10, y=140)

    entryemail = Entry(window)
    entryemail.place(x=160, y=140)

    lblgender = Label(window, text="Select Customer Gender")
    lblgender.place(x=10, y=170)

    combogender = cb(window, value=['Male', 'Female', 'Others'], width=10, height=10)
    combogender.set('Genders')
    combogender.place(x=160, y=170)

    lbladdress = Label(window, text="Enter Customer Address")
    lbladdress.place(x=10, y=200)

    entryaddress = Entry(window)
    entryaddress.place(x=160, y=200)

    lblpayment_mode = Label(window, text="Select Payment mode")
    lblpayment_mode.place(x=10, y=230)

    entrypayment_mode = cb(window, value=['Cash', 'Card', 'Others'], width=10, height=10)
    entrypayment_mode.place(x=160, y=230)

    lblpayment = Label(window, text='Enter value')
    lblpayment.place(x=10, y=260)

    entrypayment = Entry(window)
    entrypayment.place(x=160, y=260)

    def Save():  # for orders
        sales_id = sales_id_user
        cust_id = rando_id
        name = entryname.get()
        ph_no = entryph_no.get()
        email = entryemail.get()
        gender = combogender.get()
        address = entryaddress.get()
        mode = entrypayment_mode.get()
        value = entrypayment.get()
        if int(value) > 0:
            print(sales_id, cust_id, name, ph_no, email, gender, address, mode, value)
            sql = "insert into customer values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(sales_id,
                                                                                                             cust_id,
                                                                                                             name,
                                                                                                             ph_no,
                                                                                                             email,
                                                                                                             gender,
                                                                                                             address,
                                                                                                             mode,
                                                                                                             value)

            sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                           database='project', port=3306, auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(name, " Saved in DataBase")
        else:
            print("Sales cannot be negative. We don't give out loans")

    Button(window, text="Save", command=Save).pack(side=BOTTOM)
    window.mainloop()


def update():
    win1 = Toplevel()
    win1.geometry(400 * 400)
    win1.configure(bg='bisque')

    def update_name():
        window1 = Toplevel()
        window1.geometry("200x200")
        window1.configure(bg='powderblue')
        lblTitle = Label(window1, text="Update Name", font="Arial,12", bg="Yellow")
        lblTitle.pack()

        lblname = Label(window1, text="Enter Customer New Name")
        lblname.pack()
        entryname = Entry(window1)
        entryname.pack()

        lblid = Label(window1, text="Enter Customer ID")
        lblid.pack()
        entryid = Entry(window1)
        entryid.pack()

        def update1():
            name = entryname.get()
            email = entryid.get()

            print(name, email)
            sql = "update customer set name='{}' where cust_id='{}'".format(name, email)

            sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                           database='project', port=3306, auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(name, " Updated in DataBase")

        Button(window1, text="Update Name", command=update1).pack(side=BOTTOM)

    def update_phone():
        window2 = Toplevel()
        window2.geometry("200x200")
        window2.configure(bg='powderblue')
        lblTitle = Label(window2, text="Update Phone", font="Arial,12", bg="Yellow")
        lblTitle.pack()

        lblph_no = Label(window2, text="Enter Customer New Phone")
        lblph_no.pack()
        entryph_no = Entry(window2)
        entryph_no.pack()

        lblid = Label(window2, text="Enter Customer ID")
        lblid.pack()
        entryid = Entry(window2)
        entryid.pack()

        def update2():
            ph_no = entryph_no.get()
            name = entryid.get()

            print(ph_no, name)
            sql = "update customer set ph_no='{}' where cust_id='{}'".format(ph_no, name)

            sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                           database='project', port=3306, auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(ph_no, " Updated in DataBase")

        Button(window2, text="Update Phone", command=update2).pack(side=BOTTOM)

    def update_email():
        window3 = Toplevel()
        window3.geometry("200x200")
        window3.configure(bg='powderblue')
        lblTitle = Label(window3, text="Update Email", font="Arial,12", bg="Yellow")
        lblTitle.pack()

        lblemail = Label(window3, text="Enter Customer New Email")
        lblemail.pack()
        entryemail = Entry(window3)
        entryemail.pack()

        id = Label(window3, text="Enter Customer ID")
        id.pack()
        entryid = Entry(window3)
        entryid.pack()

        def update3():
            email = entryemail.get()
            name = entryid.get()

            print(email, name)
            sql = "update customer set email='{}' where cust_id='{}'".format(email, name)

            sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                           database='project', port=3306, auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(email, " Updated in DataBase")

        Button(window3, text="Update Email", command=update3).pack(side=BOTTOM)

    def update_address():
        window4 = Toplevel()
        window4.geometry("200x200")
        window4.configure(bg='powderblue')
        lblTitle = Label(window4, text="Update Address", font="Arial,12", bg="Yellow")
        lblTitle.pack()

        lbladdress = Label(window4, text="Enter Customer New Address")
        lbladdress.pack()
        entryaddress = Entry(window4)
        entryaddress.pack()

        lblid = Label(window4, text="Enter Customer ID")
        lblid.pack()
        entryid = Entry(window4)
        entryid.pack()

        def update4():
            address = entryaddress.get()
            name = entryid.get()

            print(address, name)
            sql = "update customer set address='{}' where cust_id='{}'".format(address, name)

            sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                           database='project', port=3306, auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(address, " Updated in DataBase")

        Button(window4, text="Update Address", command=update4).pack(side=BOTTOM)

    b1 = Button(win1, text="Update Customer Name", command=update_name)
    b2 = Button(win1, text="Update Customer Phone", command=update_phone)
    b3 = Button(win1, text="Update Customer Email", command=update_email)
    b4 = Button(win1, text="Update Customer Address", command=update_address)

    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()


def delete():
    root = Toplevel()

    lblname = Label(root, text="Enter Customer  ID")
    lblname.pack()

    entryname = Entry(root)
    entryname.pack()

    def DeleteIt():
        name = entryname.get()
        print(name)

        sql = "delete from customer where cust_id = '{}'".format(name)
        sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                       database='project', port=3306, auth_plugin='mysql_native_password')

        cursor = sql_connection.cursor()
        if delete_Check():
            cursor.execute(sql)
            sql_connection.commit()
            print(name, " Deleted from DataBase")
        else:
            print(name, 'Record not deleted')

    Button(root, text="Delete", command=DeleteIt).pack(side=BOTTOM)


def view():
    root2 = Toplevel()

    lblname = Label(root2, text="Select Customer ID")
    lblname.pack()
    entryname = cb(root2, value=cust_ids_customer, width=10, height=10)
    entryname.set('Choose Id')
    entryname.pack()

    def ShowIt():
        name = entryname.get()
        sql = "select * from customer where cust_id = '{}'".format(name)
        sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                       database='project', port=3306, auth_plugin='mysql_native_password')

        cursor = sql_connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    Button(root2, text="Show", command=ShowIt).pack(side=BOTTOM)


def view_all():
    sql = "select * from customer"

    sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                   database='project', port=3306, auth_plugin='mysql_native_password')

    cursor = sql_connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])


def view_sales():
    root2 = Toplevel()

    lblsales_id = Label(root2, text="Your Sales ID")
    lblsales_id.pack()

    entrysales_id = Label(root2, text=sales_id_user)
    entrysales_id.pack()

    def ShowIt():
        print(sales_id_user, ':checking sales id')

        sql = "select value from customer where sales_id = '{}'".format(sales_id_user)
        sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                       database='project', port=3306, auth_plugin='mysql_native_password')

        cursor = sql_connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        sales_list = [x[0] for x in rows]
        sales_list = list(map(int, sales_list))
        print(sales_list)
        total = sum(sales_list)
        print('Gross Sales:', total)

    Button(root2, text="Show", command=ShowIt).pack(side=BOTTOM)


def customer_all():
    win = Toplevel()
    win.geometry("400x400")
    win.configure(bg='bisque')
    lblTitle = Label(win, text="SELECT YOUR CHOICE!!!!", font="Arial,16", bg="Yellow")
    lblTitle.pack()
    b1 = Button(win, text=" Add Customer", command=add, fg="red")
    b2 = Button(win, text="Update Customer", command=update, fg="purple")
    b3 = Button(win, text="Delete Customer", command=delete, fg="orange")
    b4 = Button(win, text="View Customer", command=view, fg="green")
    b5 = Button(win, text="View All Customers", command=view_all, fg="blue")
    b6 = Button(win, text="View sales", command=view_sales, fg='IndianRed4')
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    b6.pack()


def login():
    global loginwindow, usernameentry, passwordentry, sales_id_user
    # this label notifies progress find a way so that it does not stack
    Label(loginwindow, text="loading", font="Arial,12", bg="Yellow").pack()

    user = usernameentry.get()

    password = passwordentry.get()

    userlist = list(userdict.keys())

    if user == userlist[0]:

        if userdict[user] == password:

            messagebox.showinfo("SUCCESS", "WELCOME BACK BOSS")

            loginwindow.destroy()

            # customer_all()
            manager_page()

        else:

            Label(loginwindow, text="wrong password", font="Arial,12", bg="Yellow").pack()

    elif user in userlist:

        if userdict[user] == password:

            messagebox.showinfo("SUCCESS", "WELCOME BACK " + user)
            sales_id_user = sales_ids_dict[user]
            loginwindow.destroy()

            # customer_all()
            selection()
        else:

            Label(loginwindow, text="wrong password", font="Arial,12", bg="Yellow").pack()
    else:

        Label(loginwindow, text="wrong username", font="Arial,12", bg="Yellow").pack()


def welcome_page():
    global welcome
    text1 = '''Welcome to customer relations management 

    please enter your designated username and password

    if you don\' t have the details then please contact the administration

    for a salesman: enter potential customer details as leads

    add new customers as orders

    for a manager: add,update and fire salesmen also analyse data '''
    welcome = Tk()
    # welcome.configure()
    # welcome.geometry()
    lbl = Label(welcome, text=text1)
    lbl.pack()
    okbutton = Button(welcome, text='ok', command=login_front)
    okbutton.pack()
    welcome.mainloop()

# login page starts here label and entry ko side by side kar de
def login_front():
    welcome.destroy()

    global loginwindow, usernameentry, passwordentry

    loginwindow = Toplevel()

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


def selection_leads():
    win = Toplevel()
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
    global cust_ids_leads
    window = Toplevel()
    window.geometry('300x330')
    window.configure(bg='pink')
    lb_title = Label(window, text='ADD LEADS', font="Arial,10", bg="Yellow")
    lb_title.pack()

    cust_id_lead = str(random.randint(0, 99999))
    cust_ids_leads.append(cust_id_lead)

    lblcustidname = Label(window, text='Customer ID')
    lblcustidname.place(x=10, y=20)

    lblcustid = Label(window, text=cust_id_lead)
    lblcustid.place(x=160, y=20)

    lbname = Label(window, text='Name')
    lbname.place(x=10, y=50)

    entry_lbname = Entry(window)
    entry_lbname.place(x=160, y=50)

    lblcategory = Label(window, text="Customer Type")
    lblcategory.place(x=10, y=80)

    combo_custtype = cb(window, values=['New', 'Repeating'], width=10, height=10)
    combo_custtype.set('Select')
    combo_custtype.place(x=160, y=80)

    lblph_no = Label(window, text="Phone number")
    lblph_no.place(x=10, y=110)

    entry_lblph_no = Entry(window)
    entry_lblph_no.place(x=160, y=110)

    lbl_meet = Label(window, text="Next meeting ('ddmmyy')")  # put date picker here
    lbl_meet.place(x=10, y=130)

    entry_lbl_meet = Entry(window)
    entry_lbl_meet.place(x=160, y=130)
    date_today = time.strftime("%d%m%Y")
    print(date_today)

    def Save():  # for orders
        cust_id = cust_id_lead
        name = entry_lbname.get()
        category = combo_custtype.get()
        phone = entry_lblph_no.get()
        meet = entry_lbl_meet.get()
        print(type(meet))
        print(type(date_today))
        if int(meet[2:4]) > int(date_today[2:4]) and int(meet[4:])==int(date_today[4:]) :
            print(cust_id, name, category, phone, meet)
            sql = "insert into leads values('{}','{}', '{}', '{}', '{}')".format(cust_id, name, category, phone, meet)

            sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                           database='project', port=3306, auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(name, " Saved in DataBase")
        elif int(meet[4:])>int(date_today[4:]):
            print(cust_id, name, category, phone, meet)
            sql = "insert into leads values('{}','{}', '{}', '{}', '{}')".format(cust_id, name, category, phone, meet)

            sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                           database='project', port=3306, auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(name, " Saved in DataBase")
        elif (int(meet[2:4]) == int(date_today[2:4] and int(meet[4:])==int(date_today[4:]))) and int(meet[0:3])>int(date_today[0:3]) :
            print(cust_id, name, category, phone, meet)
            sql = "insert into leads values('{}','{}', '{}', '{}', '{}')".format(cust_id, name, category, phone, meet)

            sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                           database='project', port=3306, auth_plugin='mysql_native_password')

            cursor = sql_connection.cursor()
            cursor.execute(sql)

            sql_connection.commit()

            print(name, " Saved in DataBase")
        else:
            print('Please enter a future date')

    Button(window, text="Save", command=Save).pack(side=BOTTOM)


def delete_leads():
    root = Toplevel()

    lblTitle = Label(root, text="Enter Cust_ID", font="Arial,16", bg="Yellow")
    lblTitle.pack()

    entryname = Entry(root)
    entryname.pack()

    def DeleteIt_leads():
        name = entryname.get()
        print(name)

        sql = "delete from leads where cust_id = '{}'".format(name)
        sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                       database='project', port=3306, auth_plugin='mysql_native_password')
        cursor = sql_connection.cursor()
        if delete_Check():
            cursor.execute(sql)
            print(name, 'Deleted from database')
        else:
            print(name, 'Record not deleted')

    Button(root, text="Delete", command=DeleteIt_leads).pack(side=BOTTOM)


def view_leads():
    root2 = Toplevel()
    combo = cb(root2, values=cust_ids_leads, width=15, height=20)
    combo.set('Select customer ID')
    combo.pack()

    entryname = combo.get()
    entryname.pack()

    def ShowIt():
        name = combo.get()
        print(name)

        sql = "select * from leads where cust_id = '{}'".format(name)
        sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                       database='project', port=3306, auth_plugin='mysql_native_password')

        cursor = sql_connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3], row[4])

    Button(root2, text="Show", command=ShowIt).pack(side=BOTTOM)


def view_all_leads():
    sql = "select * from leads"

    sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                   database='project', port=3306, auth_plugin='mysql_native_password')

    cursor = sql_connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3], row[4])


def add_salesman():
    win = Toplevel()
    win.geometry("400x400")
    win.configure(bg='bisque')
    Label(win, text="Enter Employee Name", bg='Yellow', fg='red').pack()
    entrykey = Entry(win)
    entrykey.pack()
    Label(win, text='Enter password', bg='yellow', fg='red').pack()
    entrypassword = Entry(win)
    entrypassword.pack()

    def process():
        key = entrykey.get()
        password = entrypassword.get()
        f2 = open('salesids','rb+')
        f = open('users', 'rb+')
        f3 = open('count_check','r+')
        sales_ids_dict = p.load(f2)
        userdict = p.load(f)
        salesidcount = f3.read()
        if key in userdict.keys():
            print('Employee already exists')
        else:
            userdict[key] = password
            f.seek(0)
            p.dump(userdict, f)
            f.flush()
            f.seek(0)
            userdict = p.load(f)
            salesidcount=str(int(salesidcount)+1)
            sales_ids_dict[key]=salesidcount
            p.dump(sales_ids_dict,f2)
            f3.write(salesidcount)
            print('EMPLOYEE ADDED:', userdict,sales_ids_dict)
        f3.flush()
        f3.close()
        f2.flush()
        f2.close()
        f.flush()
        f.close()

    Button(win, text='add', command=process).pack()

def view_sales_manager():
    win = Toplevel()
    win.geometry("400x400")
    win.configure(bg='bisque')
    Label(win, text="Enter Employee ID", bg='Yellow', fg='red').pack()
    entryid = Entry(win)
    entryid.pack()
    def ShowIt():
        print(entryid.get(), ':checking sales id')

        sql = "select value from customer where sales_id = '{}'".format(entryid.get())
        sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                       database='project', port=3306, auth_plugin='mysql_native_password')

        cursor = sql_connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        sales_list = [x[0] for x in rows]
        sales_list = list(map(int, sales_list))
        print(sales_list)
        total = sum(sales_list)
        print('Gross Sales:', total)

    Button(win, text="Show", command=ShowIt).pack(side=BOTTOM)


def update_salesman():
    update = Toplevel()
    update.geometry("400x400")
    update.configure(bg='bisque')
    Label(update, text='UPDATE MENU', bg='Yellow', fg='red').pack()
    lblold = Label(update, text='enter old username which has to be changed')
    lblold.pack()
    entryold = Entry(update)
    entryold.pack()
    f = open('users', 'rb+')
    userdict = p.load(f)

    def update_user():
        global process
        update1 = Toplevel()
        update1.geometry("400x400")
        update1.configure(bg='bisque')
        old = entryold.get()
        if old in list(userdict.keys()):
            lblold = Label(update1, text='enter new username which has to be added')
            lblold.pack()
            entrynew = Entry(update1)
            entrynew.pack()

            def process():
                if entrynew.get() in list(userdict.keys()):
                    print('This user already exists')
                else:
                    password = userdict[old]
                    del userdict[old]
                    userdict[entrynew.get()] = password
                    f.seek(0)
                    p.dump(userdict, f)
                    f.close()
                    print(userdict)
        else:
            print('username does not exist')
        Button(update1, text='done', command=process).pack()

    def update_password():
        global process2
        update2 = Toplevel()
        update2.geometry("400x400")
        update2.configure(bg='bisque')
        old = entryold.get()
        if old in list(userdict.keys()):
            lblpassnew = Label(update2, text='enter new password which has to be changed')
            lblpassnew.pack()
            entrynew = Entry(update2)
            entrynew.pack()

            def process2():
                userdict[old] = entrynew.get()
                f.seek(0)
                p.dump(userdict, f)
                f.close()
                print('success')
                print(userdict)
        else:
            print('username does not exist')
        Button(update2, text='done', command=process2).pack()

    Button(update, text='update user', command=update_user).pack()
    Button(update, text='update password', command=update_password).pack()


def fire_salesman():
    update3 = Toplevel()
    update3.geometry("400x400")
    update3.configure(bg='bisque')
    Label(update3, text='FIRE!!!', bg='Yellow', fg='red').pack()
    lblold = Label(update3, text='Enter Employee who has to be fired')
    lblold.pack()
    entryold = Entry(update3)
    entryold.pack()

    def process():
        if entryold.get() in list(userdict.keys()):
            if entryold.get()=='admin':
                print('Sorry! You cannot resign.')
            else:
                del userdict[entryold.get()]
                print('Employee fired successfully!. Nice job!')
                print(userdict)
                f = open('users', 'wb+')
                p.dump(userdict, f)
                f.flush()
                f.close()
        else:
            print('Employee doesnt exist')

    Button(update3, text='Fire!!!', command=process, bg='black', fg='red').pack()


def plots():
    plotswin = Toplevel()
    plotswin.geometry('300x300')
    plotswin.configure(bg='burlywood1')

    def total_sales_vs_salesman():
        global id_list_final, total_sales_list_final
        total_sales_list = []

        sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                       database='project', port=3306, auth_plugin='mysql_native_password')
        cursor = sql_connection.cursor()

        cursor.execute('select sales_id from customer')
        #print(cursor.fetchall())
        id_list = [x[0] for x in cursor.fetchall()]
        print('id',id_list)
        for i in id_list:
            if i not in id_list_final:
                id_list_final.append(i)
        id_list_final = list(map(int, id_list_final))
        print(id_list_final)

        for i in id_list:
            cursor.execute("select value from customer where sales_id='{}'".format(i))
            rows = cursor.fetchall()
            sales_list = [x[0] for x in rows]
            sales_list = list(map(int, sales_list))
            total = sum(sales_list)
            total_sales_list.append(total)
        for i in total_sales_list:
            if i not in total_sales_list_final:
                total_sales_list_final.append(i)
        print(total_sales_list_final)
        plt.figure()
        plt.bar(np.arange(len(id_list_final)), total_sales_list_final, align='center', alpha=0.5)
        plt.xticks(np.arange(len(id_list_final)), id_list_final)
        plt.ylabel('Total Sale in Rupees')
        plt.xlabel('Sales ID of salesman')
        plt.title('Total sales of each Salesman')

        plt.show()

    def pie_totalsales_vs_salesman():
        labels = id_list_final
        sizes = total_sales_list_final
        colors = ['red','blue','green','yellow','orange','white']
        explode = []
        for i in total_sales_list_final:
            if i > 100000:
                explode.append(0.2)
            else:
                explode.append(0)
        print(explode)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%03.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()

    def payment_method_pie():
        cash=0
        card=0
        other=0
        colors = ['red', 'blue', 'green', 'yellow', 'orange', 'white']
        explode=[]
        labels=['cash','card','other']
        sql_connection = mysql.connect(user="root", password=mysql_password, host=hostname,
                                       database='project', port=3306, auth_plugin='mysql_native_password')
        cursor = sql_connection.cursor()

        cursor.execute('select mode from customer')
        # print(cursor.fetchall())
        mode_list = [x[0] for x in cursor.fetchall()]
        print('id', mode_list)
        for i in mode_list:
            if i=='Cash':
                cash+=1
            elif i=='Card':
                card+=1
            else:
                other+=1

        sizes=[cash,card,other]

        #some error pls fix
        for i in range(0,len(sizes)-1):
            print(i)
            if sizes[i]==0:
                sizes.pop(i)
                labels.pop(i)


        print(sizes)
        for i in sizes:
            explode.append(0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%03.1f%%', shadow=True, startangle=140)
        plt.show()



    Button(plotswin, text='View Salesman vs Total Sales Graph', command=total_sales_vs_salesman).pack()
    Button(plotswin, text='View Salesman vs Total Sales Graph in Pie', command=pie_totalsales_vs_salesman).pack()
    Button(plotswin, text='Pie test', command=payment_method_pie).pack()



def manager_page():
    win = Toplevel()
    win.geometry("400x400")
    win.configure(bg='bisque')
    lblTitle = Label(win, text="SELECT YOUR CHOICE!!!!", font="Arial,16", bg="Yellow")
    lblTitle.pack()
    b1 = Button(win, text=" Add Salesman", command=add_salesman, fg="red")
    b2 = Button(win, text="Update Salesman", command=update_salesman, fg="purple")
    b3 = Button(win, text="Fire Salesman", command=fire_salesman, fg="orange")
    b4 = Button(win, text="View Customer", command=view, fg="green")
    b5 = Button(win, text="View All Customers", command=view_all, fg="blue")
    b6 = Button(win, text="View sales", command=view_sales_manager, fg='IndianRed4')
    b7 = Button(win, text='Map Graphs', command=plots, fg='Powder Blue')
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    b6.pack()
    b7.pack()


# both are same as customer only small changes
def selection():
    win = Toplevel()
    win.geometry("300x170")
    win.configure(bg='bisque')
    lblTitle = Label(win, text="SELECT YOUR CHOICE!!!!", font="Arial,16", bg="Yellow")
    lblTitle.pack()
    b1 = Button(win, text=" Leads", command=selection_leads, fg="red")
    b2 = Button(win, text="Orders", command=customer_all, fg="purple")
    b1.pack()
    b2.pack()

with open('check.txt', 'r+') as f1:
    if f1.read() == '1':
        pass
    else:
        createsalesidfile()
        createuserfile()
        f1.write('1')

import_salesids()
import_userdict()
print(userdict)
print(sales_ids_dict)
welcome_page()
