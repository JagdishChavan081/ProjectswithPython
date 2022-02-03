#importing Modules
from tkinter import *
from time import strftime


root = Tk()
root.title("Digital Clock")

#create a function to display time

def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text =string)
    lbl.after(1000, time)


#styling the label widget which display the clock
lbl = Label(root, font = "arial 100 bold", bg="black",fg="white")


lbl.pack(anchor = "center",fill = "both", expand=1)

time()

mainloop()
