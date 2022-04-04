from tkinter import *

window = Tk()

style1 = {
    "bg": "red",
    "fg": "white"
}

label_1 = Label(window, text="Lovely clocks", **style1)
label_1.pack(fill=X)

label_2 = Label(window, text="NONONO", **style1)
label_2.pack(fill=X)

label_3 = Label(window, text="Fun is in Order", **style1)
label_3.pack(fill=X)

window.mainloop()