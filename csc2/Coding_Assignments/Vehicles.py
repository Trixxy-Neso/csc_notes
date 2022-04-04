######################################################################################################################
# Name: Josephine Rei Sale
# Date: 12/20/2021
# Desc: A program looking at vehicles
######################################################################################################################

# the vehicle class
# a vehicle has a year, make, and model
class Vehicle:
    def __init__ (self, make, model): 
        self.make = make
        self.model = model

    @property 
    def make (self):
        return self._make
    @make.setter
    def make (self, value):
        self._make = value

    @property 
    def model (self):
        return self._model
    @model.setter
    def model (self, value):
        self._model = value

    @property 
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        if not hasattr (self, "_year"):
            self._year = "2000"
        if 2000 <= int(value) <= 2018:
            self._year = value


# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
v1 = Vehicle("Dodge", "Ram")
v2 = Vehicle("Honda", "Odyssey")
print("v1={} {}".format(v1.make, v1.model))
print("v2={} {}".format(v2.make, v2.model))
print()

v1.year = 2016
v2.year = 2016
print("v1={} {} {}".format(v1.year, v1.make, v1.model))
print("v2={} {} {}".format(v2.year, v2.make, v2.model))
print()

v1.year = 1999
v2.model = "Civic"
v2.year = 2007
print("v1={} {} {}".format(v1.year, v1.make, v1.model))
print("v2={} {} {}".format(v2.year, v2.make, v2.model))