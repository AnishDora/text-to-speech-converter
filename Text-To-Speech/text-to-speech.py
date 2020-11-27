import tkinter as tk
import os
from tkinter import filedialog
from gtts import gTTS

def convert():
    filename = filedialog.askopenfilename(title="Select a file", filetypes=[('TXT Files','*.txt')])
    mylabel = tk.Label(frame, text=filename)
    mylabel.place(relx=0.15, rely=0.25)
    basename = os.path.basename(filename) 
    file=open(basename)
    final=file.read()
    language='en'
    audio=gTTS(text=final,lang=language,slow=False)
    audio.save(basename+".wav")
    os.system(basename+".wav")


Height = 450
Width = 800

root = tk.Tk()


canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root, bg='#374254')
frame.place(relwidth=1, relheight=1)

button = tk.Button(frame, text="Browse your TXT file to convert", font=('Courier', 20), bd=3, bg="#d1d8e3",  command=lambda: convert())
button.place(relx=0.15, rely=0.10, relheight=0.15, relwidth=0.7)


text = tk.Label(frame, text="Welcome to text-to-speech converter", font=('Courier', 15), fg="white", bg='#374254')
text.place(relx=0.13, rely=0.65, relheight=0.5, relwidth=0.75)

root.mainloop()
