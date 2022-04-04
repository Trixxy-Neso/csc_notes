class names are UpperCamelCase

class Pikachu:
    # class viariables - for all objects in the class
    type = 'electric'


    # the constructor
    def __init__(self, nickname):
        # instance variables go here
        self.nickname = nickname
        self.flushed = '😳' #not necessarry btw, for testing purposes :)


pika_1 = Pikachu("Brad")
pika_2 = Pikachu("Rat")


print(pika_1.nickname)
print(pika_2.nickname)  #call on instance variables
print(Pikachu.type) #Call on class variables
print(pika_1.type)  #the type Electric applies to the class as a whole

pika_2.nickname = "Rodent" #reassigns nickname 
Pikachu.type = 'elec' #reassigns type.
print(Pikachu.type)
print(pika_2.type)
print(pika_2.nickname)


pika_2.type = "abc" #changes only pika_2's type
print(pika_2.type)
print(Pikachu.type)

print('🍞') #apparently emojis work in code, do with that what you will.
print(pika_2.flushed) #won't work as a variable, will get returned tho
#This has nothing to do with O.O.P