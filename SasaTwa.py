import sqlite3
from tkinter import*

VenP3=Tk()
VenP3.title("VenuePage3")
Background=PhotoImage(file='VenuePage.png')
Background1=Label(VenP3,image=Background).place(x=0,y=0)
Background2=PhotoImage(file='Sasa1.png')
Background3=Label(VenP3,image=Background2).place(x=38,y=158)
Background4=PhotoImage(file='Sasa2.png')
Background5=Label(VenP3,image=Background4).place(x=430,y=150)
Background6=PhotoImage(file='Sasa3.png')
Background7=Label(VenP3,image=Background6).place(x=833,y=150)

VenP3.maxsize(width=1240, height=720)
VenP3.minsize(width=1240,height=720)

def prev():
    VenP3.destroy()
    import Venue

def book():
    VenP3.destroy()
    import PaymentSasa

NameVen=Label(VenP3,text="SA:SA TWA", font=('Helvetica',24),bg='#FBF1EA')
NameVen.place(x=230,y=480)

LocVen=Label(VenP3,text="Location: Dhalpa,Kirtipur,Kathmandu", font=('Helvetica',14),bg='#FBF1EA')
LocVen.place(x=45,y=540)

CapVen=Label(VenP3,text="Capacity: 250", font=('Helvetica',14),bg='#FBF1EA')
CapVen.place(x=45,y=580)

ConVen=Label(VenP3,text="Contact No: 01-5907942", font=('Helvetica',14),bg='#FBF1EA')
ConVen.place(x=45,y=620)

PriceVen=Label(VenP3,text="Price: Rs.50,000/-", font=('Helvetica',14),bg='#FBF1EA')
PriceVen.place(x=45,y=650)

Ser=Label(VenP3,text="-Catering ", font=('Helvetica',14),bg='White')
Ser.place(x=950,y=500)

SerDJ=Label(VenP3,text="-DJ, Music", font=('Helvetica',14),bg='white')
SerDJ.place(x=950,y=550)

SerBar=Label(VenP3,text="-Bar", font=('Helvetica',14),bg='white')
SerBar.place(x=950,y=600)

SerPar=Label(VenP3,text="-Parking", font=('Helvetica',14),bg='white')
SerPar.place(x=950,y=650)

book_but=Button(VenP3,text='BOOK NOW',font=("Helvetica",14),bg='Green',command=book)
book_but.place(x=480,y=640)

back_but=Button(VenP3,text='<Back',font=('Helvetica',14),command=prev)
back_but.place(x=1060,y=30)

VenP3.mainloop()

