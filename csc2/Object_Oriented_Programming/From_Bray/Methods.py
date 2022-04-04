class Pikachu:
    # class viariables - for all objects in the class
    type = 'electric'
    description = "A yellow rat."


    # the constructor
    def __init__(self, nickname):
        self.nickname = nickname
        self.level = 1
        self.hp = 10

    # instance methods
    def level_up(self):
        self.level += 1
    
    def full_heal(self):
        self.hp = 10

    def __str__(self): #Magic method, or something, calls when you print., tells it what to print (ex: print(pika1))
        result = ''     #create the string
        result += f"Nickname: {self.nickname} " #adds to the string
        result += f"\nLevel: {self.level} " 
        return result   

    #class methods - apply to the class as a whole, class is an implicit argument
    @classmethod 
    def set_description(cls, new_description): #typically use cls, like using 'self'
        cls.description = new_description
    
    #static method - no implicit arguments
    @staticmethod
    def weak_against(type):
        return type in ['ground', 'Ground']

    
pika1 = Pikachu('Gauss') #Weird nickname ik
print(pika1.level)
pika1.level_up()
print(pika1.level)
print(pika1)
print(pika1.__str__()) #can be called manually, same as last line

Pikachu.set_description('An electric yellow rat') #uses class method

print(Pikachu.weak_against('flying')) #uses static method:returns false
print(Pikachu.weak_against('ground')) #returns true
