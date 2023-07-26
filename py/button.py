from tkinter import *
from tkinter import messagebox
 
nut = Tk()
nut.geometry("200x200")
 
def clickLeftButton():
    messagebox.showinfo("Hello world", "Left Button clicked")
 
def clickRightButton():
    messagebox.showinfo("Hello world", "Right Button clicked")
 
b1 = Button(nut, text = "Left", command = clickLeftButton, activeforeground = "red", activebackground = "silver", pady = 10)
b2 = Button(nut, text = "Right", command = clickRightButton, activeforeground = "red", activebackground = "silver", pady = 10)
b3 = Button(nut, text = "Top", activeforeground = "red", activebackground = "silver", pady = 10)
b4 = Button(nut, text = "Below", activeforeground = "red", activebackground = "silver", pady = 10)
b1.pack(side = LEFT)
b2.pack(side = RIGHT)
b3.pack(side = TOP)
b4.pack(side = BOTTOM)
nut.mainloop()