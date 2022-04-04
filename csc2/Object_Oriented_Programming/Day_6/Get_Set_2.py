class Pikachu:
    # class viariables - for all objects in the class
    type = 'electric'
    description = "A yellow rat."


    # the constructor
    def __init__(self, nickname):
        print('Constsuctor')
        self.nickname = nickname
        self.level = 1
        self.hp = 10

    #Getters/Accessors
    @property
    def nickname(self):
        #really specify how you want it to return the nickname
        print('Getter/Accessor')
        return self._nickname

    @property
    def level(self):
        return self._level


    #Setters/Mutators
    @nickname.setter
    def nickname(self, new_nickname):
        print('Setter/Mutator')
        if new_nickname in ['💩', '🤬','doodoo', 'nonoword']:
            self._nickname = '*****'
        else:
            self._nickname = new_nickname
        
    @level.setter
    def level(self, value):
        if value < 1:
            self._level = 1
        else:
            self._level = value


    #additional methods
    def level_up(self):
        self.level += 1
    
    def full_heal(self):
        self.hp = 10

    def __str__(self): #Magic method, or something, calls when you print., tells it what to print (ex: print(pika1))
        result = ''     #create the string
        result += f"Nickname: {self.nickname} " #adds to the string
        result += f"\nLevel: {self.level} " 
        return result   

pika1 = Pikachu('💩')
print(pika1.nickname)
pika1.nickname = 'Jordan'

print()
pika1.level = 10
print(pika1)
pika1.level = -10
print(pika1)
