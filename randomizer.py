import tkinter as tk
from tkinter import *

window = tk.Tk()
chrValues = []

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

# Regular Character Checkboxes
chrIsaac = tk.IntVar()
chrIsaacBox = tk.Checkbutton(checkBoxes, text="Isaac",
                       variable=chrIsaac, onvalue=1, offvalue=0, bg="white")
chrIsaacBox.grid(row=0, sticky=W)

chrMaggy = tk.IntVar()
chrMaggyBox = tk.Checkbutton(checkBoxes, text="Magdalene",
                       variable=chrMaggy, onvalue=1, offvalue=0, bg="white")
chrMaggyBox.grid(row=1, sticky=W)

chrCain = tk.IntVar()
chrCainBox = tk.Checkbutton(checkBoxes, text="Cain",
                       variable=chrCain, onvalue=1, offvalue=0, bg="white")
chrCainBox.grid(row=2, sticky=W)

chrJudas = tk.IntVar()
chrJudasBox = tk.Checkbutton(checkBoxes, text="Judas",
                       variable=chrJudas, onvalue=1, offvalue=0, bg="white")
chrJudasBox.grid(row=3, sticky=W)

chrBlueBaby = tk.IntVar()
chrBlueBabyBox = tk.Checkbutton(checkBoxes, text="Blue Baby",
                       variable=chrBlueBaby, onvalue=1, offvalue=0, bg="white")
chrBlueBabyBox.grid(row=4, sticky=W)

chrEve = tk.IntVar()
chrEveBox = tk.Checkbutton(checkBoxes, text="Eve",
                       variable=chrEve, onvalue=1, offvalue=0, bg="white")
chrEveBox.grid(row=5, sticky=W)

chrSamson = tk.IntVar()
chrSamsonBox = tk.Checkbutton(checkBoxes, text="Samson",
                       variable="Samson", onvalue=1, offvalue=0, bg="white")
chrSamsonBox.grid(row=6, sticky=W)

chrAzazel = tk.IntVar()
chrAzazelBox = tk.Checkbutton(checkBoxes, text="Azazel",
                       variable=chrAzazel, onvalue=1, offvalue=0, bg="white")
chrAzazelBox.grid(row=7, sticky=W)

chrLazarus = tk.IntVar()
chrLazarusBox = tk.Checkbutton(checkBoxes, text="Lazarus",
                       variable=chrLazarus, onvalue=1, offvalue=0, bg="white")
chrLazarusBox.grid(row=8, sticky=W)

chrEden = tk.IntVar()
chrEdenBox = tk.Checkbutton(checkBoxes, text="Eden",
                       variable=chrEden, onvalue=1, offvalue=0, bg="white")
chrEdenBox.grid(row=9, sticky=W)

chrLost = tk.IntVar()
chrLostBox = tk.Checkbutton(checkBoxes, text="The Lost",
                       variable=chrLost, onvalue=1, offvalue=0, bg="white")
chrLostBox.grid(row=10, sticky=W)

chrLilith = tk.IntVar()
chrLilithBox = tk.Checkbutton(checkBoxes, text="Lilith",
                       variable=chrLilith, onvalue=1, offvalue=0, bg="white")
chrLilithBox.grid(row=11, sticky=W)

chrKeeper = tk.IntVar()
chrKeeperBox = tk.Checkbutton(checkBoxes, text="Keeper",
                       variable=chrKeeper, onvalue=1, offvalue=0, bg="white")
chrMaggyBox.grid(row=12, sticky=W)

chrApollyon = tk.IntVar()
chrApollyonBox = tk.Checkbutton(checkBoxes, text="Apollyon",
                       variable=chrApollyon, onvalue=1, offvalue=0, bg="white")
chrApollyonBox.grid(row=13, sticky=W)

chrForgotten = tk.IntVar()
chrForgottenBox = tk.Checkbutton(checkBoxes, text="The Forgotten",
                       variable=chrForgotten, onvalue=1, offvalue=0, bg="white")
chrForgottenBox.grid(row=14, sticky=W)

chrBeth = tk.IntVar()
chrBethBox = tk.Checkbutton(checkBoxes, text="Bethany",
                       variable=chrBeth, onvalue=1, offvalue=0, bg="white")
chrBethBox.grid(row=15, sticky=W)

chrJacob = tk.IntVar()
chrJacobBox = tk.Checkbutton(checkBoxes, text="Jacob and Esau",
                       variable=chrJacob, onvalue=1, offvalue=0, bg="white")
chrJacobBox.grid(row=16, sticky=W)

# Tainted Character Checkboxes
chrTIsaac = tk.IntVar()
chrTIsaacBox = tk.Checkbutton(checkBoxes, text="Tainted Isaac",
                       variable=chrTIsaac, onvalue=1, offvalue=0, bg="white")
chrTIsaacBox.grid(row=0, column=1, sticky=W)

confirm = tk.Button(window, text="Confirm Selection")
confirm.pack()

randomize = tk.Button(window, text="Randomize")
randomize.pack()

window.mainloop()
