from tkinter import *
WIDTH = 300
HEIGHT = 300
window = Tk()

label_1 = Label(window, text="Lovely clocks", bg="#aef9ff", fg="#f07e00")
label_1.pack(side = LEFT, fill = X)

label_2 = Label(window, text="NONONO", bg="#000000", fg="#FFFFFF")
label_2.pack(side = LEFT, expand = 1, fill = BOTH)

label_3 = Label(window, text="Fun is in Order", bg="#CCAA99", fg="#123456")
label_3.pack(fill = Y)

window.geometry (f"{WIDTH}x{HEIGHT}")
window.mainloop()