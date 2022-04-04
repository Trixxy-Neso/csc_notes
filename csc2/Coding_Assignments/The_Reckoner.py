from tkinter import *

button_data = [
    {"row": 1, "col": 0, "value": "("}, 
    {"row": 1, "col": 1, "value": ")"},
    {"row": 1, "col": 2, "value": "AC"},
    {"row": 1, "col": 3, "value": "**"},

    {"row": 2, "col": 0, "value": "7"}, 
    {"row": 2, "col": 1, "value": "8"},
    {"row": 2, "col": 2, "value": "9"},
    {"row": 2, "col": 3, "value": "/"},
    
    {"row": 3, "col": 0, "value": "4"}, 
    {"row": 3, "col": 1, "value": "5"},
    {"row": 3, "col": 2, "value": "6"},
    {"row": 3, "col": 3, "value": "*"},

    {"row": 4, "col": 0, "value": "1"}, 
    {"row": 4, "col": 1, "value": "2"},
    {"row": 4, "col": 2, "value": "3"},
    {"row": 4, "col": 3, "value": "-"},

    {"row": 5, "col": 0, "value": "0"}, 
    {"row": 5, "col": 1, "value": "."},
    {"row": 5, "col": 2, "value": "="},
    {"row": 5, "col": 3, "value": "+"},
]

USING_PI = False

class ReckonerGUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        if USING_PI:
            master.attributes ("-fullscreen", True)
        self.setupGUI()
        self.pack (fill=BOTH, expand = 1)



    def make_button(self, row, col, value):
        bg_color = "#cccccc"
        if value == "=":
            bg_color = "blue"

        button = Button(self,
            text = value, 
            bg=bg_color,
            width=5,
            activebackground="white",
            command= lambda: self.handle_button_press(value)
        )
        button.grid(row=row, column=col, sticky=NSEW)

    def setupGUI (self):
        # set up display & geometry
        self.display = Label (self, text = "", anchor=E, bg="white", fg="black", height=1)
        self.display.grid (row=0, column=0, columnspan=4, sticky=NSEW)


        # configure rows & column
        for row in range (7):
            Grid.rowconfigure(self, row, weight=1)
        for col in range (4):
            Grid.columnconfigure(self, col, weight=1)


        #create buttons
        for button in button_data:
            self.make_button (button["row"], button ["col"], button ["value"])

        # more geometry
        

        # keep track of error and calculation
        self.error = False
        self.calc = False

    def handle_button_press (self, button_value):
        display = self.display["text"]
        clear = button_value == "AC"
        evaluate = button_value == "="
        numeric = button_value in list ("1234567890")

        if clear:
            self.display["text"] = ""
            return

        if evaluate:
            try:
                result = str(eval(display))
                self.dispay["text"] = result
                self.calc = True
            except:
                self.display ["text"] = "ERROR"
                self.error = True
            return

        if self.error:
            self.error = False
            self.display ["text"] = ""
            return

        if self.calc and numeric:
            self.calc = False
            self.display ["text"] += button_value
            return

        self.display["text"] += button_value
        self.calc = False
        return


window = Tk()
window.title("Reckoner")
r = ReckonerGUI(window)
window.mainloop()

