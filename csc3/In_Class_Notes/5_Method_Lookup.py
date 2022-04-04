class Shape: 
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def draw (self, space=False):
        for i in range (0, self.length):
            print ('*' * self.width)
        if space == True:
            print()
            

class Rectangle (Shape):
    def __init__(self, length, width):
        Shape.__init__(self, length, width)

class Square (Shape):
    def __init__(self, length):
        Shape.__init__(self, length, length)

class Triangle (Shape):
    def __init__(self, length):
        Shape.__init__(self, length, length)

    def draw (self, space=False):
        l = self.width
        for i in range (0, self.length):
            print ('*' * l)
            l -= 1
        if space == True:
            print ()

y = Rectangle (4, 5)
y.draw()

t = Triangle (5)
t.draw()