# Abstract Methods  -   Methods intended for subclasses

class Animal:
    def __init__ (self):
        """Constructor"""

    def communicate (self):
        raise NotImplementedError("Communicate not Implemented in Subclass")

class Bird:
    def __init__ (self):
        """Whatever a bird has"""

    def communicate (self):
        print ("Chirp!")

import abc

class Pokemon(metaclass=abc.ABCMeta):
    def __init__ (self):
        """This"""

    @abc.abstractclassmethod
    def communicate (self):
        "whatever"

class Raboot (Pokemon):

    def __init__(self):
        "HopScotch"

    def communicate(self):
        print ("Hnnn... Hnn!")


HopScotch = Raboot()
HopScotch.communicate()

