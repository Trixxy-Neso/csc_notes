class Pikachu:
    # class variables
    type = 'electric'
    # Constructor
    def __init__(self, nickname):
        # instance variables
        self.nickname = nickname
        self.flushed = '😳' #not necessarry 




pika_1 = Pikachu("Remi")
pika_2 = Pikachu("Joshua")

print (f"A wild pikachu, {pika_1.nickname}, has appeared!")

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