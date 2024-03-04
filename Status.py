from tkinter import *
from tkinter import ttk
import sqlite3

def retrieve_data():
    try:
        con = sqlite3.connect('Status.db')
        c = con.cursor()

        # Execute a SELECT query to retrieve data from the table
        c.execute("SELECT * FROM data")

        # Fetch all rows returned by the query
        rows = c.fetchall()

        # Insert data into the Treeview
        for row in rows:
            tree.insert("", "end", values=row)

    except sqlite3.Error as e:
        print('Error:', e)

    finally:
        if con:
            con.close()

# def delete_item():
#     try:
#         selected_item = tree.selection()[0]
#         tree.delete(selected_item)

#         con = sqlite3.connect('Status.db')
#         c = con.cursor()

#         # Get the ID of the selected item
#         selected_id = tree.item(selected_item)['values'][0]

#         # Execute a DELETE query to remove data from the table
#         c.execute("DELETE FROM data WHERE ID=?", (selected_id,))

#         # Commit the changes
#         con.commit()

#     except Exception as e:
#         print('Error:', e)

#     finally:
#         if con:
#             con.close()

def on_status_click():
    tree.delete(*tree.get_children())  # Clear existing data
    retrieve_data()

def delete():
    con=sqlite3.connect('Status.db')
    c=con.cursor()
    c.execute('DELETE FROM data WHERE ID='+ent_del.get())
    con.commit()
    con.close()
    ent_del.delete(0,END)

def edit():
    global editor
    editor=Tk()
    editor.title("Update details")
    editor.geometry('300x400')
    con=sqlite3.connect('Status.db')
    c=con.cursor()
    record_id=ent_up.get()
    c.execute("SELECT * FROM data WHERE  ID=?",(record_id,))
    records= c.fetchall()
    
    # global NameEnt
    # global ContEnt
    global DatEnt
    global TimEnt
    # NameEnt = Entry(editor, width=30)
    # NameEnt.grid(row=0, column=1, padx=20, pady=(10, 0))
    # ContEnt = Entry(editor, width=30)
    # ContEnt.grid(row=0, column=1, padx=20, pady=(10, 0))
    DatEnt = Entry(editor, width=30)
    DatEnt.grid(row=0, column=1, padx=20, pady=(10, 0))
    TimEnt = Entry(editor, width=30)
    TimEnt.grid(row=1, column=1)

    DatLab=Label(editor, text="Date : ")
    DatLab.grid(row=0,column=0)
    TimLab=Label(editor,text="Time : ")
    TimLab.grid(row=1,column=0)

    for record in records:
            DatEnt.insert(0,record[3])
            TimEnt.insert(0,record[4])
    
    ent_up.delete(0,END)
    btn_save = Button(editor, text='SAVE', command=lambda:update(record_id))  #record
    btn_save.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

def update(record_id):
    con = sqlite3.connect('Status.db')
    c = con.cursor()
    c.execute('''
        UPDATE data SET
            date=:d,
            time=:t
        WHERE ID =:id ''', 
        {
            'd': DatEnt.get(),
            't': TimEnt.get(),
            'id': record_id
        }
    )
    con.commit()
    con.close()
    editor.destroy()








xs = Tk()
xs.title("Venue Signup")
bckgd = PhotoImage(file='9.png')
background_label = Label(xs, image=bckgd)
background_label.place(x=0, y=0)
xs.maxsize(width=1240, height=720)
xs.minsize(width=1240, height=720)

# Create a Treeview widget
tree = ttk.Treeview(xs)
tree.place(relx=0.6, rely=0.5, anchor="center")

# Define columns for the Treeview
tree["columns"] = ("ID", "Name", "Contact ID", "Date", "Time")

# Format columns
tree.column("#0", width=0, stretch=NO)  # Hide the first blank column
tree.column("ID", anchor=CENTER, width=100)
tree.column("Name", anchor=W, width=200)
tree.column("Contact ID", anchor=W, width=150)
tree.column("Date", anchor=W, width=150)
tree.column("Time", anchor=W, width=150)

# Define column headings
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Contact ID", text="Contact ID")
tree.heading("Date", text="Date")
tree.heading("Time", text="Time")

# Add status button
status_button = Button(xs, text="Status", command=on_status_click, font=("Helvetica", 25), fg='#ffffff', bg='#fce9dc', bd=0.5)
status_button.place(x=80, y=200)

# Add delete button
delete_button = Button(xs, text="Delete", font=("Helvetica", 25), fg='#ffffff', bg='#fce9dc', bd=0.5, command=delete)
delete_button.place(x=80, y=400)

ent_del=Entry(xs,width=10, bg='#fce9dc')
ent_del.place(x=110,y=360,height=30)

update_button= Button(xs, text="Update", font=("Helvetica", 14), fg='#000000', bg='#FFFFFF', bd=0.5, command=edit)
update_button.place(x=1000,y=478)

ent_up=Entry(xs,font=("Arial", 16), width=10, bg='#fce9dc')
ent_up.place(x=870,y=485)

xs.mainloop()
