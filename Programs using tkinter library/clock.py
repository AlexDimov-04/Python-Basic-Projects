# import modules
from tkinter import *
from tkinter.ttk import *
from time import strftime

# main root window with title
root = Tk()
root.title("Clock")


# function for the time pass
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


# initializing the label geometry
label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()

# run the root
root.mainloop()
