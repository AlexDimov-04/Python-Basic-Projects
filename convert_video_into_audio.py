# import modules
import moviepy.editor
from tkinter.filedialog import *

# ask from the user for a video file
video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)

# extract the audio from the video file
audio = video.audio
# name the audio file
audio.write_audiofile("sample.mp3")

# print the output message for a successful convert
print("Successfully converted!")
