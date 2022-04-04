from random import randint, seed

# pseudo-random: appears random but is deterministic.

print (randint (0,100))
print (randint (0,100))   

seed (123456)
print (randint (0,100))
print (randint (0,100))

