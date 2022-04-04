class Bread:
    def __init__ (self, flour_type, is_moldy=False):
        self.flour_type = flour_type
        self.is_moldy = is_moldy

    def __str__(self):
        return f"Flour: {self.flour_type}; Moldy: {self.is_moldy}"

class SaleItem:
    def __init__ (self, price):
        self.price = price

    def __str__ (self):
        return f"Price: ${self.price}"

class HamburgerBun (Bread, SaleItem):
    def __init__(self):
        Bread.__init__(self, 'Wheat')
        SaleItem.__init__(self, 3.50)

    def __str__ (self):
        return Bread.__str__(self) + '; ' + SaleItem.__str__(self)

b = HamburgerBun()
print (b)