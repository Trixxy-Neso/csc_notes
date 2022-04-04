# Filter - define fuction that returns Boolean based on input
    # Pass function through filter (func, list)

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

a_list = [1, 2, 44, 6, 7, 3, 768]

filtered_list = list(filter(is_even, a_list))
print (filtered_list)


# Map - define function that manipulates input
    # Map returns manipulated data

def double (x):
    return x * 2

data = [1, 2, 3, 4, 5, 6, 7, 8]
doub_val = list (map (double, data))
print (doub_val)


# Reduce - runs func with first two data points, then result w/ next, etc.
from functools import reduce
def concatenate (x, y):
    return x + ' ' + y

a_list = ['hi','how','are','you','?']
reduced_ = reduce (concatenate, a_list)
print (reduced_)