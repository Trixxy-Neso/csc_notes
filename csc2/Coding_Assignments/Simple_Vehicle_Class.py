################################################################
####    Name:   Josephine Rei Sale                          ####
####    Date:   2 - 19 - 2022                               ####
####    Desc:   Implements vehicle, truck and car classes.  ####
################################################################

# the vehicle class
class Vehicle:
    # vehicle has year, make, model
    def __init__ (self, make, model):
        self.make = make
        self.model = model
        self.year = 2000
        # default year == 2000

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
    # limit available years to target range
    def year(self, value):
        if 2000 <= int(value) <= 2018:
            self._year = value
        else:
            pass

    def __str__(self):
        return (f"{self.year} {self.make} {self.model}")


# the truck class
# a truck is a vehicle
class Truck (Vehicle):
    def __init__ (self, make, model):
        Vehicle.__init__ (self, make, model)


# the car class
# a car is a vehicle
class Car (Vehicle):
    def __init__ (self, make, model):
        Vehicle.__init__ (self, make, model)



# the Dodge Ram class
# a Dodge Ram is a truck
# all Dodge Rams have the same make and model
class DodgeRam (Truck):
    make = "Dodge"
    model = "Ram"
    def __init__ (self, year, make=None, model=None):
        Truck.__init__(self, DodgeRam.make, DodgeRam.model)
        Truck.year = year

    
# the Honda Civic class
# a Honda Civic is a car
# all Honda Civics have the same make and model
class HondaCivic (Car):
    make = "Honda"
    model = "Civic"
    def __init__ (self, year, make=None, model=None):
        Car.__init__(self, HondaCivic.make, HondaCivic.model)
        Car.year = year



# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
ram = DodgeRam(2016)
print(ram)

civic1 = HondaCivic(2007)
print(civic1)

civic2 = HondaCivic(1999)
print(civic2)