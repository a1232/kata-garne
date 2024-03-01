# from tkinter import*
# from tkinter import messagebox
# import sqlite3


# def verify():
#     email = Entry1.get()
#     password = Entry2.get()
#     try:
#         conI = sqlite3.connect("DataEntry.db")
#         curI = conI.cursor()
#         curI.execute("CREATE TABLE IF NOT EXISTS data(email TEXT, password TEXT)")
#         curI.execute("SELECT email FROM data WHERE email=?", [email])
#         result = curI.fetchone()
#         if result:
#             stored_password = curI.execute("SELECT password FROM data WHERE email=?", [email]).fetchone()
#             if stored_password and stored_password[0] == password:
#                 messagebox.showinfo("Verification", "Login successful!")
#                 Kg.destroy()
#                 import new
#             else:
#                 messagebox.showerror("Verification", "Invalid Password")
#         else:
#             messagebox.showerror("Verification", "Invalid email")
#         conI.commit()
#         conI.close()
#     except Exception as e:
#         messagebox.showerror("Verification", f"Error: {e}")


# Kg= Tk()
# Kg.title("Kata Garne? Logins")
# Backgrnd=PhotoImage(file='KGPR6.png')
# Backgrnd1=Label(Kg,image=Backgrnd).place(x=0,y=0)
# Kg.maxsize(width=1240, height=720)
# Kg.minsize(width=1240,height=720)



# Customer_mail= Label(Kg, text="E-mail:",font=('helvetica',18,'bold'),bg='#f8f5ee')
# Customer_mail.place(x=800,y=200)
# Entry1=Entry(Kg,width=25,font=("helvetica",12,'italic'))
# Entry1.place(x=910,y=208)
# Customer_password= Label(Kg,text="Password:",font   =('helvetica',18,'bold'),bg='#f8f5ee')
# Customer_password.place(x=780,y=250)
# Entry2= Entry(Kg,width=25,font=("helvetica",12,'italic'),show="*")
# Entry2.place(x=910,y=258)

# def pas():
#     if pH.get()==1:
#         Entry2.config(show="")
#     else:
#         Entry2.config(show="*")
# pH=IntVar()
# showPH=Checkbutton(Kg,text="Show Password",width=15, font=("helvetica", 12, 'italic'),command=pas, variable=pH, onvalue=1 ,bg="#f8f5ee")
# showPH.place(x=930,y=300)

# Update=Button(Kg,text="Signin",width=25,font=('helvetica',10,'bold'),command=verify).place(x=880,y=350)
# Seperate=Label(Kg,text="OR \n LOGIN USING:",font=('helvetica',10,'bold'),bg='#f8f5ee').place(x=940,y=400)
# Fb=Button(Kg,text="Facebook",width=25,bg="Blue",fg="white",font=('helvetica',11,'bold')).place(x=870,y=460)
# Gl=Button(Kg,text="Google+",width=25,bg="Red",fg='white',font=('helvetica',11,'bold')).place(x=870,y=510)

# label = Label(Kg, text='').pack()

# Kg.mainloop()



from tkinter import *
from tkinter import messagebox
import tkinter as tk
def update_entry_with_data(selected_date):
    venue_entry.delete(0, tk.END)
    venue_entry.insert(0, selected_date)

# Read selected date from file
with open("selected_date.txt", "r") as file:
    selected_date = file.read()

# Create the main window
root = tk.Tk()
root.title("Venue Input")

# Load the image
image_path = "venue_portal.png"
image = tk.PhotoImage(file=image_path)

# Create a Canvas widget
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=image)

#Create an Entry widget
venue_entry = tk.Entry(root)
venue_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
update_entry_with_data(selected_date)
root.mainloop()   









