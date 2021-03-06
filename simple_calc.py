#simple calculator with light and dark theme -- using python - tkinter

#importing tkinter
from tkinter import *
import tkinter
root=Tk()

root.config(background="#D9D7F1")
root.title("Simple Calculator")


e=Entry(root,width=35,borderwidth=5)



#button functionality

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number)) 
    

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_number
    global math
    math="add"
    f_number=int(first_number)
    e.delete(0,END)

def button_sub():
    first_number=e.get()
    global f_number
    global math
    math="sub"
    f_number=int(first_number)
    e.delete(0,END)
    

def button_mul():
    first_number=e.get()
    global f_number
    global math
    math="mul"
    f_number=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_number
    global math
    math="div"
    f_number=int(first_number)
    e.delete(0,END)
    return




def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_number+int(second_number))
    elif math=="sub":
        e.insert(0,f_number-int(second_number))
    elif math=="mul":
        e.insert(0,f_number*int(second_number))
    else:
        e.insert(0,f_number/int(second_number))



def darkmode():
    root.config(background="#393E46")
    button_0.config(bg="#393E46",fg="white")
    button_1.config(bg="#393E46",fg="white")
    button_2.config(bg="#393E46",fg="white")
    button_3.config(bg="#393E46",fg="white")
    button_4.config(bg="#393E46",fg="white")
    button_5.config(bg="#393E46",fg="white")
    button_6.config(bg="#393E46",fg="white")
    button_7.config(bg="#393E46",fg="white")
    button_8.config(bg="#393E46",fg="white")
    button_9.config(bg="#393E46",fg="white")

    button_add.config(bg="#0D7377",fg="white")
    button_sub.config(bg="#0D7377",fg="white")
    button_mul.config(bg="#0D7377",fg="white")
    button_div.config(bg="#0D7377",fg="white")
    button_equal.config(bg="#0D7377",fg="white")
    




def lightmode():
    root.config(background="#D9D7F1")
    button_0.config(bg="#D9D7F1",fg="black")
    button_1.config(bg="#D9D7F1",fg="black")
    button_2.config(bg="#D9D7F1",fg="black")
    button_3.config(bg="#D9D7F1",fg="black")
    button_4.config(bg="#D9D7F1",fg="black")
    button_5.config(bg="#D9D7F1",fg="black")
    button_6.config(bg="#D9D7F1",fg="black")
    button_7.config(bg="#D9D7F1",fg="black")
    button_8.config(bg="#D9D7F1",fg="black")
    button_9.config(bg="#D9D7F1",fg="black")

    button_add.config(bg="#B6FFCE",fg="black")
    button_sub.config(bg="#B6FFCE",fg="black")
    button_mul.config(bg="#B6FFCE",fg="black")
    button_div.config(bg="#B6FFCE",fg="black")
    button_equal.config(bg="#B6FFCE",fg="black")


#defining buttons
button_mode=Button(root,text="dark mode")
button_1= Button(root, text="1", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(1))
button_2= Button(root, text="2", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(2))
button_3= Button(root, text="3", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(3))
button_4= Button(root, text="4", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(4))
button_5= Button(root, text="5", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(5))
button_6= Button(root, text="6", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(6))
button_7= Button(root, text="7", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(7))
button_8= Button(root, text="8", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(8))
button_9= Button(root, text="9", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(9))
button_0= Button(root, text="0", padx=30,pady=20 ,bg="#D9D7F1",command=lambda:button_click(0))
button_add= Button(root, text="+", padx=30,pady=20 ,bg="#B6FFCE", command=button_add)
button_sub= Button(root, text="-", padx=30,pady=20 ,bg="#B6FFCE", command=button_sub)
button_mul= Button(root, text="*", padx=30,pady=20 ,bg="#B6FFCE", command=button_mul)
button_div= Button(root, text="/", padx=30,pady=20 ,bg="#B6FFCE", command=button_div)

button_equal= Button(root, text="=", padx=30,pady=20,bg="#B6FFCE" ,command=button_equal)


button_clear= Button(root, text="clear",padx=20, pady=20,bg="#FF8080" ,command=button_clear)

button_darkmode=Button(root,text="dark",padx=60,pady=10,bg="#393E46",fg="white",command=darkmode)
button_lightmode=Button(root,text="light",padx=60,pady=10,command=lightmode)

#grid arangement of elements

#row 0

e.grid(row=0,column=0,columnspan=4,padx=10,pady=20)

#row 1

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_div.grid(row=1,column=3)

#row 2
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_mul.grid(row=2,column=3)

#row 3

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_sub.grid(row=3,column=3)



#row 4

button_clear.grid(row=4,column=0)
button_0.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_add.grid(row=4,column=3)

#row 5
button_darkmode.grid(row=5,column=0,columnspan=2)
button_lightmode.grid(row=5,column=2, columnspan=2)


root.mainloop()
