from tkinter import *
from tkinter.simpledialog import askstring
import tkinter.messagebox
import pyrebase
from fpdf import FPDF
from datetime import date

#Firebase Configuration---------------------------------------------------------------------
config={
    "apiKey": "AIzaSyBCN51h67sT_3BCpaNSKNLzerOCxdseP4Y",
    "authDomain": "hospital-199fc.firebaseapp.com",
    "databaseURL": "https://hospital-199fc-default-rtdb.firebaseio.com",
    "projectId": "hospital-199fc",
    "storageBucket": "hospital-199fc.appspot.com",
    "messagingSenderId": "539786147277",
    "appId": "1:539786147277:web:be627abbf2a53d92b80084",
    "measurementId": "G-HHX9X0MVTH"
  }
#-------------------------------------------------------------------------------------------

#Initialize Firebase------------------------------------------------------------------------
global db
firebase = pyrebase.initialize_app(config)
db=firebase.database()
#-------------------------------------------------------------------------------------------

#Initialize---------------------------------------------------------------------------------
app=Tk()
app.geometry('400x210')
app.title('The Bug Slayers')
mlabel=Label(app, text="DocsApp+", bg='white', font=('consolas', 24, 'bold'),fg='green')
mlabel.pack(side=TOP)
app.config(background='white')
#-------------------------------------------------------------------------------------------

#Functions----------------------------------------------------------------------------------
def his():
    pass

def pescribe():
    status=["-select-","General","Restricted"]
    global db
    user=askstring('Unique Id','Patient Unique Id')
    pes_no=(db.child(user).child("Prescription").shallow().get()).val()
    pes_no=list(pes_no)
    pes_no=pes_no[-1]
    nm=str((db.child(user).child("Name").get()).val())
    pes=(db.child(user).child("Prescription").get()).val()
    year=(str(pes[-1]["Date"]).split("-"))[-1]
    age=int(year)-int((db.child(user).child("Age").get()).val())
    sex=str((db.child(user).child("Sex").get()).val())
    dat=str(pes[-1]["Date"])

    m=Tk()
    m.geometry("600x480")
    m.title("Prescription")
    mlabel=Label(m, text="Prescription", bg='white', font=('consolas', 20, 'bold'),fg='red')
    mlabel.pack(side=TOP)
    m.config(background='white')
    st=StringVar(m)
    st.set(status[0])

    nlabel=Label(m,text="Name",font=('consolas', 15, 'bold'),bg="white")
    nlabel.place(x=10,y=50)
    name=Label(m,text=nm,font=('consolas', 15, 'bold'),bg="white")
    name.place(x=150,y=50)
    dlabel=Label(m,text="Age",font=('consolas', 15, 'bold'),bg="white")
    dlabel.place(x=10,y=80)
    year=Label(m,text=str(age),font=('consolas', 15, 'bold'),bg="white")
    year.place(x=150,y=80)
    slabel=Label(m,text="Sex",font=('consolas', 15, 'bold'),bg="white")
    slabel.place(x=10,y=110)
    sx=Label(m,text=sex,font=('consolas', 15, 'bold'),bg="white")
    sx.place(x=150,y=110)
    slabel=Label(m,text="Date",font=('consolas', 15, 'bold'),bg="white")
    slabel.place(x=10,y=140)
    sx=Label(m,text=dat,font=('consolas', 15, 'bold'),bg="white")
    sx.place(x=150,y=140)
    ndlabel=Label(m,text="Doctor",font=('consolas', 15, 'bold'),bg="white")
    ndlabel.place(x=10,y=170)
    doc=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    doc.place(x=150,y=170)
    dialabel=Label(m,text="Diagnosis",font=('consolas', 15, 'bold'),bg="white")
    dialabel.place(x=10,y=220)
    diag=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    diag.place(x=150,y=220)
    plabel=Label(m,text="Place",font=('consolas', 15, 'bold'),bg="white")
    plabel.place(x=10,y=270)
    place=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    place.place(x=150,y=270)
    stlabel=Label(m,text="Status",font=('consolas', 15, 'bold'),bg="white")
    stlabel.place(x=10,y=320)
    sts=OptionMenu(m,st,*status)
    sts.config(bg='slategray1',width=35,bd=4,font=("consolas",14,'bold'),relief='sunken')
    sts.place(x=150,y=320)
    mdlabel=Label(m,text="Medication",font=('consolas', 15, 'bold'),bg="white")
    mdlabel.place(x=10,y=370)
    med=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    med.place(x=150,y=370)

    def click_pes():
        dia=str(diag.get())
        doctor=str(doc.get())
        pl=str(place.get())
        stat=str(st.get())
        meds=str(med.get()).split(",")
        medic=[None]+meds
        temp_data={
            "Date":dat,
            "Diagnosis":dia,
            "Doctor":doctor,
            "Medication":medic,
            "place:":pl,
            "Status":stat
        }
        db.child(user).child("Prescription").child(pes_no).set(temp_data)
        m.destroy()
        tkinter.messagebox.showinfo("Successful", "Prescription is Successfully Uploaded!")

    pes_But=Button(m,padx=10,pady=3,bd=4,bg='royalblue1',text="Upload",font=("Courier New",15,'bold'),width=10,command=click_pes)
    pes_But.place(x=250,y=420)
    

    mainloop()

#Initial Screen-----------------------------------------------------------------------------
butreg=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="Update History",font=("Courier New",18,'bold'),width=25)
butreg.place(x=10,y=50)
butgen=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="Prescribe",font=("Courier New",18,'bold'),width=25,command=pescribe)
butgen.place(x=10,y=100)
butpes=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="History & Prescriptions",font=("Courier New",18,'bold'),width=25)
butpes.place(x=10,y=150)
#-------------------------------------------------------------------------------------------

app.mainloop()
