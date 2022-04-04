from tkinter import *

window = Tk()       # window is a Tk object
text = Label(window, text="Hello World")
                    # creates a label widget and attaches to window
text.pack(fill=X)         # pack is a geometry manager

window.mainloop