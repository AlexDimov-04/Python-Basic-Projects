# import modules
import tkinter as tk
from tkinter.filedialog import *
import pyautogui

# initializing the root and the geometry
root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()


# function for the screenshot method
def take_screenshot():
    my_screenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    my_screenshot.save(save_path + "screenshot.png")


# creating the button_pattern
button_pattern = tk.Button(text="Take Screenshot", command=take_screenshot, font=10)
canvas.create_window(150, 150, window=button_pattern)

# run the root
root.mainloop()
