from tkinter import *

WIDTH = 300
HEIGHT = 300
window = Tk()

label_1 = Label(window, text="Hello to those lost.", bg="#aef9ff", fg="#f07e00")
label_1.grid(row = 0, column = 0)

label_2 = Label(window, text="I hope you are better than I.", bg="#000000", fg="#FFFFFF")
label_2.grid(row = 1, column = 0)

entry_1 = Entry(window)
entry_1.grid (row = 0, column = 6)

entry_2 = Entry(window)
entry_2.grid (row = 1, column = 17)


window.geometry = (f"{WIDTH}x{HEIGHT}")
window.mainloop()