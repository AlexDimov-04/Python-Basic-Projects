# import modules
import PIL
from PIL import Image
from tkinter.filedialog import *

# ask the image path from the user
file_path = askopenfilename()
# set the image to the pillow library
img = PIL.Image.open(file_path)
# geometry for the image
height, width = img.size

# compress the image
img = img.resize((height, width), PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()

# save the compressed image
img.save(save_path+"compressed.jpg")
