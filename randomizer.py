import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title("The Binding of Isaac: Repentance Randomizer")
window.resizable(width=False, height=False)

canvas = tk.Canvas(window, height=800, width=800, bg="#E9E7DF")
canvas.pack()

checkBoxes = tk.Frame(window, bg="white")
checkBoxes.place(relwidth=0.825, relheight=0.825, relx=0.05, rely=0.05)

testVar = tk.IntVar()
check = tk.Checkbutton(checkBoxes, text="Test Box",
                       variable=testVar, onvalue=1, offvalue=0)
check.grid(row=0)

window.mainloop()
