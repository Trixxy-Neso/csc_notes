# Probability a value between 0.00 and 1.00

num_sides = 20
side_with_20 = 1
side_with_7 = 1

chance_of_20 = side_with_20 / num_sides
chance_of_7 = side_with_7 / num_sides

print (f"The probability of rolling a 20 on a d20 is {chance_of_20}, or {chance_of_20 * 100}%")
print (f"The probability of rolling a 7 on a d20 is {chance_of_7}, or {chance_of_7 * 100}%")

from random import randint

probabilities = [0]*6

rolls = 10000

for i in range (rolls):
    value = randint (1,6)
    probabilities [value - 1] += 1

for i in range (len(probabilities)):
    probabilities [i] = probabilities [i] / rolls

print (probabilities)

# sum of two d6

frequencies = [0] * 11

print ('Die 1\tDie 2\tSum')

for die1 in range (1,7):
    for die2 in range (1,7):
        dice_sum = die1 + die2
        frequencies [dice_sum - 2] += 1
        print (f"{die1}\t{die2}\t{dice_sum}")

print (frequencies)
print ("\nSum\tFreq\tProb")
for i in range (len(frequencies)):
    print (f"{i+2}\t{frequencies[i]}\t{frequencies [i] / sum(frequencies)}")


# Probability of Flipping Coins
    # Get Two Heads     1/4     25%
    # Get Two Tails     1/4     25%
    # Get One of Each   1/2     50%