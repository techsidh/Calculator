from tkinter import *
import random
from tkinter import messagebox

val=" "
operator=" "
store_bvalue=0
def btn1_isclicked():
    global val
    val=val + "1"
    data.set(val)

def btn2_isclicked():
    global val
    val=val +"2"
    data.set(val)

def btn3_isclicked():
    global val
    val=val +"3"
    data.set(val)

def btn4_isclicked():
    global val
    val=val +"4"
    data.set(val)

def btn5_isclicked():
    global val
    val=val +"5"
    data.set(val)

def btn6_isclicked():
    global val
    val=val +"6"
    data.set(val)

def btn7_isclicked():
    global val
    val=val +"7"
    data.set(val)

def btn8_isclicked():
    global val
    val=val +"8"
    data.set(val)

def btn9_isclicked():
    global val
    val=val +"9"
    data.set(val)

def btn0_isclicked():
    global val
    val=val +"0"
    data.set(val)

def btn_plus():
    global store_bvalue
    global operator
    global val
    store_bvalue=int(val)
    operator="+"
    val=val + "+"
    data.set(val)

def btn_minus():
    global operator
    global val
    global store_bvalue
    store_bvalue=int(val)
    operator="-"
    val=val + "-"
    data.set(val)

def btn_mul():
    global operator
    global val
    global store_bvalue
    store_bvalue=int(val)
    operator="*"
    val=val + "*"
    data.set(val)

def btn_div():
    global operator
    global val
    global store_bvalue
    store_bvalue=int(val)
    operator="/"
    val=val + "/"
    data.set(val)

def c_pressed():
    global operator
    global val
    global store_bvalue
    val = " "
    store_bvalue =0
    operator =" "
    data.set(val)


def equal_bn():
    global operator
    global val
    global store_bvalue
    val2=val

    if operator == "+":
        x = int(val2.split("+")[1])
        val=store_bvalue + x    #i use same val variable to get value and also here to store the count
        data.set(val)
        val=str(val)

    elif operator == "-":
        x = int(val2.split("-")[1])
        val=store_bvalue - x
        data.set(val)
        val=str(val)
    elif operator == "*":
        x=int(val2.split("*")[1])
        val=store_bvalue * x
        data.set(val)
        val=str(val)
    elif operator == "/":
        x=int(val2.split("/")[1])
        if x==0:
            messagebox.showerror("Error","Undefine value")
            store_bvalue = ""
            val =" "
            data.set(val)
        else:
            val=int(store_bvalue/x)
            data.set(val)
            val=str(val)








root= Tk()
root.geometry("240x240")
root.title("Calculator")
root.resizable(0,0)
data=StringVar()
lab1=Label(root,
           text="Label",
           font=("calibri 22"),
           anchor=SE,
           textvariable=data,
           background="#ffffff",
           fg="#000000",).pack(expand=True,fill="both")
btnframe1=Frame(root,bg="#00FF00")
btnframe1.pack(expand=True,fill="both",)

btnframe2=Frame(root)
btnframe2.pack(expand=True,fill="both",)

btnframe3=Frame(root)
btnframe3.pack(expand=True,fill="both",)

btnframe4=Frame(root)
btnframe4.pack(expand=True,fill="both")

btn1=Button(btnframe1,text="1",command=btn1_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn2=Button(btnframe1,text="2",command=btn2_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn3=Button(btnframe1,text="3",command=btn3_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn4=Button(btnframe1,text="+",relief=GROOVE,borde=0,command=btn_plus).pack(side=LEFT,expand=True,fill="both")

btn5=Button(btnframe2,text="4",command=btn4_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn6=Button(btnframe2,text="5",command=btn5_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn7=Button(btnframe2,text="6",command=btn6_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btb8=Button(btnframe2,text="-",relief=GROOVE,borde=0,command=btn_minus).pack(side=LEFT,expand=True,fill="both")

btn9=Button(btnframe3,text="7",command=btn7_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn10=Button(btnframe3,text="8",command=btn8_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn11=Button(btnframe3,text="9",command=btn9_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn12=Button(btnframe3,text="/",relief=GROOVE,borde=0,command=btn_div).pack(side=LEFT,expand=True,fill="both")

btn13=Button(btnframe4,text="C",relief=GROOVE,borde=0,command=c_pressed).pack(side=LEFT,expand=True,fill="both")
btn14=Button(btnframe4,text="0",command=btn0_isclicked,relief=GROOVE,borde=0).pack(side=LEFT,expand=True,fill="both")
btn15=Button(btnframe4,text="*",relief=GROOVE,borde=0,command=btn_mul).pack(side=LEFT,expand=True,fill="both")
btn16=Button(btnframe4,text="=",relief=GROOVE,borde=0,command=equal_bn).pack(side=LEFT,expand=True,fill="both")


root.mainloop()