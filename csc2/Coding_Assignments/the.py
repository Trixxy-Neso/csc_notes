class House:
    def __init__(self, size = None):
        self.size = size
        print ("A")

    @property
    def size(self):
        print("B")
        return self._size

    @size.setter
    def size(self, value):
        print ("C")
        self._size = value

    def price (self):
        print ("D")
        return self.size * 150

h1 = House()
print("E")
h2 = House(2000)
print (h1.size)
print (h2.price())