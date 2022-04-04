# Consider: number of ways to form pairs from 10 people
#       n!/n!(n-1)!     ncr     10 choose 2
#       Start with base case
#   Total People        Ways
#       1                0
#       2                1
#       3                3
#       4                6
#       5               10
#       6               15
#       7               21
#       8               28
#       9               36
#      10               45

def ways (number):
    x = 0
    while number > 0:
        number -= 1
        x += number
    print (x)

#def ways2 (number):
#    if number == 0:
#        return 1
#    else:
#        return ways2 (number - 1)

ways (2)

ways (10)

def f (x, n):
    if n == 0: 
        return 1
    else:
        return x * f(x, n-1)


def fib (pos):
    if pos == 1:
        return 0
    elif pos == 2:
        return 1
    else:
        return fib (pos - 1) + fib (pos - 2)


for num in range (1, 5):
    print (fib (num))