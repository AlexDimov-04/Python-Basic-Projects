# import module
from tkinter import *


# function for the prime or non-prime number logic
def prime_or_not_prime():
    global text
    number = int(entry_window.get())
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                text.set(f"{number} is not a Prime Number!")
                break
        else:
            text.set(f"{number} is a Prime Number!")
    else:
        text.set(f"{number} is not a Prime Number!")


# initializing the window and the geometry
window = Tk()
window.title("Prime Number Checker")
window.geometry("350x150")

# initializing the label
label = Label(window, text="Type a Number", font=100)
label.pack()

# initializing the entry_window
entry_window = Entry(window, width=40, borderwidth=5)
entry_window.pack()

# initializing the button_check
button_check = Button(window, text="Check", command=prime_or_not_prime)
button_check.pack()

# declare the text as a global variable
text = StringVar()
number_type = Label(window, textvariable=text)
number_type.pack()

# run the program
window.mainloop()
