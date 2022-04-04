############################################
####    Name:   Josephine Rei Sale      ####
####    Date:   3-25-2022               ####
####    Desc:   A Room for Adventures   ####
############################################

from tkinter import *

WIDTH = 800
HEIGHT = 600

class Room:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grab = []
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grab(self):
        return self._grab
    @grab.setter
    def grab(self, value):
        self._grab = value

    # methods
    def add_exit (self, item, desc):
        pass
    def add_grab (self, item, desc):
        pass
    def del_grab (self, item, desc):
        pass
    def __str__(self):
        pass

class Game (Frame):
    def __init__ (self, parent):
        pass

    def create_rooms(self):
        pass

    def set_up_GUI(self):
        pass

    def set_image(self):
        pass

    def play(self):
        self.create_rooms()
        self.set_up_GUI()
        self.set_image()
        self.set_status("")

    def process(self, event):
        pass

window = Tk()
window.title("Room Adventure Revolutions")
game = Game(window)
game.play()
window.mainloop()