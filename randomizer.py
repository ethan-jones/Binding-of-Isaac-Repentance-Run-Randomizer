import tkinter as tk
from tkinter import *
import characters

window = tk.Tk()
chrValues = [tk.IntVar()] * 34


window.title("The Binding of Isaac: Repentance Randomizer")
window.resizable(width=False, height=False)

# Functions
def randomizeCharacters():
    print("Test")

def confirmSelection():
    print("Test")
        

canvas = tk.Canvas(window, height=800, width=800, bg="#E9E7DF")
canvas.pack()

checkBoxes = tk.Frame(window, bg="white")
checkBoxes.place(relwidth=0.825, relheight=0.825, relx=0.08, rely=0.05)

i = 0
j = 0
for chr in characters.list:
    if (i == 16):
        i = 0
        j = 1
    tk.Checkbutton(checkBoxes, text=chr.name, variable=chrValues[i],
                   onvalue=1, offvalue=0, bg="white").grid(row=i, column=j, sticky=W)
    i = i + 1
     

confirm = tk.Button(window, text="Confirm Selection")
confirm.pack()

randomize = tk.Button(window, text="Randomize")
randomize.pack()

window.mainloop()
