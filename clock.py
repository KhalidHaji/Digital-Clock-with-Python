from tkinter import *
from tkinter import Label, Tk

from time import strftime

root=Tk()
root.title("SAACAD")
root.geometry("350x150")
root.resizable(0,0)


text_font=("ds-digital",50)
background = "#f2e750"
foreground= "#363529"
border_width = 25

def time_clock():
    string= strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, time_clock)

label = Label(root, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)


time_clock()

root.mainloop()