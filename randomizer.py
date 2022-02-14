from distutils import command
import tkinter as tk
from tkinter import *
import characters
import random

window = tk.Tk()
chrValues = []
for i in range(34):
    chrValues.append(tk.IntVar())
    
enabledCharacters = []
chrBoxes = []


window.title("The Binding of Isaac: Repentance Randomizer")
window.resizable(width=False, height=False)



# Functions
def randomizeCharacters():
    enabledCharacters.clear()
    for i in range(34):
        if (chrValues[i].get() == 1):
            enabledCharacters.append(characters.list[i])
    print(random.choice(enabledCharacters).name)
 
def selectAll():
    for chr in chrBoxes:
        chr.select()
        
def deselectAll():
    for chr in chrBoxes:
        chr.deselect()



canvas = tk.Canvas(window, height=800, width=800, bg="#E9E7DF")
canvas.pack()

checkBoxes = tk.Frame(window, bg="white")
checkBoxes.place(relwidth=0.825, relheight=0.825, relx=0.08, rely=0.05)

i = 0
j = 0
val = 0
for chr in characters.list:
    if (i == 16):
        i = 0
        j = 1
    chrBoxes.append(tk.Checkbutton(checkBoxes, text=chr.name, variable=chrValues[val],
                   onvalue=1, offvalue=0, bg="white"))
    chrBoxes[val].grid(row=i, column=j, sticky=W)
    i = i + 1
    val = val + 1
     
     
selectAllButton = tk.Button(checkBoxes, text="Select All", command=selectAll)
selectAllButton.grid(row=17, column=0, sticky=E)

deselectAllButton = tk.Button(checkBoxes, text="Deselect All", command=deselectAll)
deselectAllButton.grid(row=17, column=1, sticky=W)
     
randomize = tk.Button(window, text="Randomize", command=randomizeCharacters)
randomize.pack()

window.mainloop()
