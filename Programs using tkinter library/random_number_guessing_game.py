# import modules
from tkinter import *
import random

# set a number for the attempts
attempts = 10

# set a variable for each wrong guess
wrong_guess_count = 0

# range of numbers to guess
answer = random.randrange(1, 100)


# function that checks the answer and describe the logic
def check_answer():
    global attempts
    global text
    global wrong_guess_count

    attempts -= 1
    guess = int(entry_window.get())

    if answer == guess:
        text.set(f"You win! Congrats!! It took you {wrong_guess_count} attempts!")
        button_check.pack_forget()
    elif attempts == 0:
        text.set("Sorry, you lost! You are out of attempts!")
        wrong_guess_count += 1
        button_check.pack_forget()
    elif guess < answer:
        text.set(f"Incorrect answer! You have {attempts} remaining, Guess higher!")
        wrong_guess_count += 1
    elif guess > answer:
        text.set(f"Incorrect answer! You have {attempts} remaining, Guess lower!")
        wrong_guess_count += 1


# initializing the root and the geometry
root = Tk()

root.title("Guess a number between 1 & 100")
root.geometry("500x150")

# initializing the label
label = Label(root, text="Guess a number between 1 & 100", font=50)
label.pack()

# initializing the entry_window
entry_window = Entry(root, width=40, borderwidth=6)
entry_window.pack()

# adding a "Check" button
button_check = Button(root, text="Check", command=check_answer)
button_check.pack()

# adding a "Quit" button
button_quit = Button(root, text="Quit", command=root.destroy)
button_quit.pack()

# adding a text for the remaining attempts
text = StringVar()
text.set("You have 10 attempts to guess the number! Go!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

# run the root
root.mainloop()
