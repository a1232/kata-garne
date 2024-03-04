from tkinter import*
from tkinter import messagebox
import sqlite3

def verify():
    email = Entry1.get()
    password = Entry2.get()
    if email=="" or password==" ":
        messagebox.showerror("Warning!","All field must be filled")
    else:
     try:
        conI = sqlite3.connect("DataEntry.db")
        curI = conI.cursor()
        curI.execute("CREATE TABLE IF NOT EXISTS data(email TEXT, password TEXT)")
        curI.execute("SELECT email FROM data WHERE email=?", [email])
        result = curI.fetchone()
        if result:
            stored_password = curI.execute("SELECT password FROM data WHERE password=?", [password]).fetchone()
            if stored_password and stored_password[0] == password:
                messagebox.showinfo("Verification", "Login successful!")
                Kg.destroy()
                import Venue
            else:
                messagebox.showerror("Verification", "Invalid Password")
        else:
            messagebox.showerror("Verification", "Invalid email")
        conI.commit()
        conI.close()
     except Exception as e:
        messagebox.showerror("Verification", f"Error: {e}")
def prev():
    Kg.destroy()
    import portal
Kg= Tk()
Kg.title("Kata Garne? Login")
Backgrnd=PhotoImage(file='KGPR6.png')
Backgrnd1=Label(Kg,image=Backgrnd).place(x=0,y=0)
Kg.maxsize(width=1240, height=720)
Kg.minsize(width=1240,height=720)

Customer_mail= Label(Kg, text="E-mail:",font=('helvetica',18,'bold'),bg='#f8f5ee')
Customer_mail.place(x=800,y=230)
Entry1=Entry(Kg,width=25,font=("helvetica",12,'italic'))
Entry1.place(x=910,y=238)
Customer_password= Label(Kg,text="Password:",font   =('helvetica',18,'bold'),bg='#f8f5ee')
Customer_password.place(x=780,y=290)
Entry2= Entry(Kg,width=25,font=("helvetica",12,'italic'),show="*")
Entry2.place(x=910,y=298)

def pas():
    if pH.get()==1:
        Entry2.config(show="")
    else:
        Entry2.config(show="*")
pH=IntVar()
showPH=Checkbutton(Kg,text="Show Password",width=15, font=("helvetica", 12, 'italic'),command=pas, variable=pH, onvalue=1 ,bg="#f8f5ee")
showPH.place(x=930,y=370)

Update=Button(Kg,text="Signin",width=25,font=('helvetica',10,'bold'),command=verify).place(x=900,y=420)
back_but=Button(Kg,text='<Back',font=('Helvetica',14),command=prev)
back_but.place(x=10,y=20)

Kg.mainloop()
