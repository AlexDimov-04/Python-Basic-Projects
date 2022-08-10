# import modules
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# read the PDF file
book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
# return the page number of the PDF file
pages = pdfreader.numPages

# read the whole data from the pages
for n in range(0, pages):
    page = pdfreader.getPage(n)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
