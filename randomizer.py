import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title("The Binding of Isaac: Repentance Randomizer")
window.resizable(width=False, height=False)

canvas = tk.Canvas(window, height=800, width=800, bg="#E9E7DF")
canvas.pack()


window.mainloop()
