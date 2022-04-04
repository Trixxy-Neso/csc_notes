# types of vehicles - cars, trucks, cycles
# types of cycle - bike, moter
# we care about - # of tires, owner, if engine

class vehicle:
    def __init__ (self, type, owner, engine=True, tires=4)
        self.type = type
        self.owner = owner
        self.engine = engine
        self.tires = tires

    @property 
    def type (self):
        return self._type
    @type.setter 
    def type (self, value):
        return self._type = value

    @property 
    def owner (self):
        return self._owner
    @owner.setter 
    def owner (self, value):
        return self._owner = value

    @property 
    def engine (self):
        return self._engine
    @engine.setter 
    def engine (self, value):
        return self._engine = value

    @property 
    def tires (self):
        return self._tires
    @tires.setter 
    def tires (self, value):
        return self._tires = value

