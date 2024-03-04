import sqlite3
from tkinter import *
from tkinter import messagebox
import re
import os

Pay = Tk()
Background = PhotoImage(file='Payment.png')
Background1 = Label(Pay, image=Background).place(x=0, y=0)
Pay.maxsize(width=1240, height=720)
Pay.minsize(width=1240, height=720)

con = sqlite3.connect('Status.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT,
    cont        TEXT,
    date        TEXT,
    time        TEXT                                       
)''')
con.commit()
con.close()


def add():
    if not all((NameEnt.get(), ContEnt.get(), DatEnt.get(), TimEnt.get())):
        messagebox.showerror("Error", "All fields must be filled")
        return
    elif len(ContEnt.get()) != 10:
        messagebox.showerror("Error!", "Please enter a valid phone number")
        return
    elif not re.match(r'\d{2}/\d{2}/\d{4}', DatEnt.get()):
        messagebox.showerror('Error!', "Please enter a valid date in day/month/year format")
        return
    elif not re.match(r'\d{1,2}:\d{1,2}-\d{1,2}:\d{1,2}', TimEnt.get()):
        messagebox.showerror('Error!', 'Enter time in a valid format (e.g., 11-14)')
        return
    else:
        try:
            con = sqlite3.connect('Status.db')
            c = con.cursor()
            c.execute("SELECT * FROM data WHERE cont=?", (ContEnt.get(),))
            if c.fetchone():
                messagebox.showerror('Error!', 'This contact number is already taken')
            else:
                c.execute("SELECT * FROM data WHERE time=?", (TimEnt.get(),))
                if c.fetchone():
                    messagebox.showerror('Error!', 'This time already exists in the database')
                else:
                    c.execute('INSERT INTO data(name, cont, date, time) VALUES(?,?,?,?)',
                              (NameEnt.get(), ContEnt.get(), DatEnt.get(), TimEnt.get()))
                    con.commit()
                    messagebox.showinfo('Success', 'Record added successfully!')
                    NameEnt.delete(0, END)
                    ContEnt.delete(0, END)
                    DatEnt.delete(0, END)
                    TimEnt.delete(0, END)
        except sqlite3.Error as e:
            messagebox.showerror('Error!', f'Failed to connect to the database. Error: {e}')
        finally:
            con.close()

def prev():
    Pay.destroy()
    os.system("python ClassicVen.py")

back_but=Button(Pay,text='Back',font=('Helvetica',14),command=prev)
back_but.place(x=1160,y=20)

NameEnt = Entry(Pay, width=25, bg='#F6DFCE')
NameEnt.place(x=700, y=153)

ContEnt = Entry(Pay, width=25, bg='#F6DFCE')
ContEnt.place(x=735, y=200)

VenEnt = Label(Pay,text="Classic Venue",font=("Helvetica",12), bg='#F8F5EE')
VenEnt.place(x=700, y=245)

DatEnt = Entry(Pay, width=25, bg='#F6DFCE')
DatEnt.place(x=700, y=295)

TimEnt = Entry(Pay, width=25, bg='#F6DFCE')
TimEnt.place(x=700, y=345)

Pay_But = Button(Pay, text="Book Now!", font=("Helvetica", 12), bg='Green', command=add)
Pay_But.place(x=780, y=480)

Pay.mainloop()