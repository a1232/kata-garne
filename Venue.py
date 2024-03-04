import sqlite3
from tkinter import *
import os

Ven = Tk()
Ven.title("HomePage")
Background = PhotoImage(file='Templet2.png')
Background1 = Label(Ven, image=Background).place(x=0, y=0)
Background2 = PhotoImage(file='Classic.png')
Background3 = Label(Ven, image=Background2).place(x=80, y=300)
Background4 = PhotoImage(file='download.png')
Background5 = Label(Ven, image=Background4).place(x=515, y=290)
Background6 = PhotoImage(file='SASAP.png')
Background7 = Label(Ven, image=Background6).place(x=890, y=300)

Ven.maxsize(width=1240, height=720)
Ven.minsize(width=1240, height=720)

# Label
det_name1 = Label(Ven, text="Classic Venue", font=('Helvetica', 20), bg='#FCE9DC')
det_name1.place(x=140, y=530)

det_add1 = Label(Ven, text="Sanepa,Lalitpur", font=('Helvetica', 16), bg='#FCE9DC')
det_add1.place(x=85, y=585)

det_rat1 = Label(Ven, text="Ratings: 4.5/5", font=('Arial', 16), bg='#FCE9DC')
det_rat1.place(x=85, y=615)

det_name2 = Label(Ven, text="Thapa Party Palace", font=('Helvetica', 20), bg='#FCE9DC')
det_name2.place(x=520, y=530)

det_add2 = Label(Ven, text="Suryabinayak,Bhaktapur", font=('Helvetica', 16), bg='#FCE9DC')
det_add2.place(x=490, y=585)

det_rat2 = Label(Ven, text="Ratings: 4/5", font=('Arial', 16), bg='#FCE9DC')
det_rat2.place(x=490, y=615)

det_name3 = Label(Ven, text="SASA Twa", font=('Helvetica', 20), bg='#FCE9DC')
det_name3.place(x=980, y=530)

det_add3 = Label(Ven, text="Kirtpur,Kathmandu", font=('Helvetica', 16), bg='#FCE9DC')
det_add3.place(x=890, y=585)

det_rat3 = Label(Ven, text="Ratings: 4/5", font=('Arial', 16), bg='#FCE9DC')
det_rat3.place(x=890, y=615)

setting = Label(Ven, text='Settings:', font=('Helvetica', 20), bg='#F6DFCE')
setting.place(x=250, y=170)

con = sqlite3.connect('DataEntry.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    email       TEXT UNIQUE,
    password    TEXT,
    cont        TEXT                   
)''')
con.commit()
con.close()

def delete():
    con=sqlite3.connect('DataEntry.db')
    c=con.cursor()
    c.execute('DELETE FROM data WHERE ID='+ent_del.get())
    con.commit()
    con.close()
    ent_del.delete(0,END)
    

def edit():
    global editor
    editor = Tk()
    editor.title('Update Data')
    editor.geometry('300x400')
    con = sqlite3.connect('DataEntry.db')
    c = con.cursor()
    record_id = ent_up.get() 
    c.execute('SELECT * FROM data WHERE ID=?', (record_id,))
    records= c.fetchall() #fetchall
    print(records)  

    global email_editor
    global password_editor
    global contact_editor

    email_editor = Entry(editor, width=30)
    email_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    password_editor=Entry(editor,width=30)
    password_editor.grid(row=1,column=1)

    contact_editor=Entry(editor,width=30)
    contact_editor.grid(row=2,column=1)

    email_label = Label(editor, text="Email")
    email_label.grid(row=0, column=0, pady=(10, 0))

    password_label=Label(editor,text="Password")
    password_label.grid(row=1,column=0)

    contact_label=Label(editor,text="Contact")
    contact_label.grid(row=2,column=0)

    if records:
        for record in records:
            email_editor.insert(0,record[1])
            password_editor.insert(0,record[2])
            contact_editor.insert(0, record[3])  
    else:
        email_editor.insert(0,'Email not found')
        password_editor.insert(0,"Password not found")
        contact_editor.insert(0, "Contact not found")

    ent_up.delete(0, END)
    btn_save = Button(editor, text='SAVE', command=lambda:update(record_id))  #record
    btn_save.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


def update(record_id):#recordid
    con = sqlite3.connect('DataEntry.db')
    c = con.cursor()
    c.execute('''
        UPDATE data SET
              email=:e,
              password=:p, 
              cont=:c
               WHERE ID =:id ''', 
               {
                   'e': email_editor.get(),
                   'p': password_editor.get(),
                   'c': contact_editor.get(),
                   'id': record_id
               }
    )
    con.commit()
    con.close()
    editor.destroy()

def logout():
    exit()

def m1():
    Ven.destroy()
    os.system("python ClassicVen.py")

def m2():
    Ven.destroy()
    os.system("python ThapaPP.py")

def m3():
    Ven.destroy()
    os.system("python SasaTwa.py")



# Buttons
btn_det1 = Button(Ven, text="More Details", font=('Arial', 14), bg='#FCE9DC',command=m1)
btn_det1.place(x=155, y=655)

btn_det2 = Button(Ven, text="More Details", font=('Arial', 14), bg='#FCE9DC',command=m2)
btn_det2.place(x=580, y=655)

btn_det3 = Button(Ven, text="More Details", font=('Arial', 14), bg='#FCE9DC',command=m3)
btn_det3.place(x=980, y=655)

btn_up = Button(Ven, text='Update Details', font=('Ariel', 16), bg='#F6DFCE', fg='black', command=edit)
btn_up.place(x=630, y=165)

btn_log = Button(Ven, text='Logout', font=('Ariel', 14), bg='#F6DFCE', fg='red',command=logout)
btn_log.place(x=900, y=165)

btn_del = Button(Ven,text="Delete Acoount", font=('Ariel',10),command=delete)
btn_del.place(x=1020,y=30)

ent_up = Entry(Ven, text='Update Details', font=('Ariel', 16), width=20, bg='#F6DFCE', fg='black')
ent_up.place(x=370, y=176)

ent_del=Entry(Ven,width=3)
ent_del.place(x=990,y=30,height=30)


Ven.mainloop()
