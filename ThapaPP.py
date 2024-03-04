import sqlite3
from tkinter import*

VenP2=Tk()
VenP2.title("VenuePage3")
Background=PhotoImage(file='VenuePage.png')
Background1=Label(VenP2,image=Background).place(x=0,y=0)
Background2=PhotoImage(file='TPP1.png')
Background3=Label(VenP2,image=Background2).place(x=37,y=170)
Background4=PhotoImage(file='TPP2.png')
Background5=Label(VenP2,image=Background4).place(x=445,y=145)
Background6=PhotoImage(file='TPP3.png')
Background7=Label(VenP2,image=Background6).place(x=850,y=143)

VenP2.maxsize(width=1240, height=720)
VenP2.minsize(width=1240,height=720)

def prev():
    VenP2.destroy()
    import Venue

def book():
    VenP2.destroy()
    import PaymentThapa

NameVen=Label(VenP2,text="Thapa Party Palace", font=('Helvetica',24),bg='#FBF1EA')
NameVen.place(x=200,y=480)

LocVen=Label(VenP2,text="Location: Near Suryavinayak Academy, Suryavinayak, Bhaktapur", font=('Helvetica',14),bg='#FBF1EA')
LocVen.place(x=45,y=540)

CapVen=Label(VenP2,text="Capacity: 300", font=('Helvetica',14),bg='#FBF1EA')
CapVen.place(x=45,y=580)

ConVen=Label(VenP2,text="Contact No:  01-4491730", font=('Helvetica',14),bg='#FBF1EA')
ConVen.place(x=45,y=620)

PriceVen=Label(VenP2,text="Price: Rs.75,000/-", font=('Helvetica',14),bg='#FBF1EA')
PriceVen.place(x=45,y=650)

Ser=Label(VenP2,text="-Catering ", font=('Helvetica',14),bg='White')
Ser.place(x=950,y=500)

SerDJ=Label(VenP2,text="-DJ, Music", font=('Helvetica',14),bg='white')
SerDJ.place(x=950,y=550)

SerBar=Label(VenP2,text="-Bar", font=('Helvetica',14),bg='white')
SerBar.place(x=950,y=600)

SerPar=Label(VenP2,text="-Parking", font=('Helvetica',14),bg='white')
SerPar.place(x=950,y=650)

book_but=Button(VenP2,text='BOOK NOW',font=("Helvetica",14),bg='Green',command=book)
book_but.place(x=480,y=640)

back_but=Button(VenP2,text='<Back',font=('Helvetica',14),command=prev)
back_but.place(x=1060,y=30)

VenP2.mainloop()

