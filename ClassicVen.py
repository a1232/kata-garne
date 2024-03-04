import sqlite3
from tkinter import*

VenP1=Tk()
VenP1.title("VenuePage3")
Background=PhotoImage(file='VenuePage.png')
Background1=Label(VenP1,image=Background).place(x=0,y=0)
Background2=PhotoImage(file='Classic2.png')
Background3=Label(VenP1,image=Background2).place(x=37,y=170)
Background4=PhotoImage(file='classic1.png')
Background5=Label(VenP1,image=Background4).place(x=430,y=165)
Background6=PhotoImage(file='Classic3.png')
Background7=Label(VenP1,image=Background6).place(x=850,y=167)

VenP1.maxsize(width=1240, height=720)
VenP1.minsize(width=1240,height=720)

def prev():
    VenP1.destroy()
    import Venue

def book():
    VenP1.destroy()
    import PaymentClassic

NameVen=Label(VenP1,text="CLASSIC VENUE", font=('Helvetica',24),bg='#FBF1EA')
NameVen.place(x=200,y=480)

LocVen=Label(VenP1,text="Location: Sanepa,Lalitpur", font=('Helvetica',14),bg='#FBF1EA')
LocVen.place(x=45,y=540)

CapVen=Label(VenP1,text="Capacity: 350", font=('Helvetica',14),bg='#FBF1EA')
CapVen.place(x=45,y=580)

ConVen=Label(VenP1,text="Contact No: 01-5905744", font=('Helvetica',14),bg='#FBF1EA')
ConVen.place(x=45,y=620)

PriceVen=Label(VenP1,text="Price: Rs.1,50,000/-", font=('Helvetica',14),bg='#FBF1EA')
PriceVen.place(x=45,y=650)

Ser=Label(VenP1,text="-Catering ", font=('Helvetica',14),bg='White')
Ser.place(x=950,y=500)

SerDJ=Label(VenP1,text="-DJ, Music", font=('Helvetica',14),bg='white')
SerDJ.place(x=950,y=550)

SerBar=Label(VenP1,text="-Bar", font=('Helvetica',14),bg='white')
SerBar.place(x=950,y=600)

SerPar=Label(VenP1,text="-Parking", font=('Helvetica',14),bg='white')
SerPar.place(x=950,y=650)

book_but=Button(VenP1,text='BOOK NOW',font=("Helvetica",14),bg='Green',command=book)
book_but.place(x=480,y=640)

back_but=Button(VenP1,text='<Back',font=('Helvetica',14),command=prev)
back_but.place(x=1060,y=30)


VenP1.mainloop()

