#####################################################
#####   Name:   Josephine Rei Sale              #####
#####   Date:   12/8/2021                       #####
#####   Desc:   A Program to Count the Zeros    #####
#####           from 0 to a Given Number        #####
#####################################################

from time import time           # in order to measure time

def count (num):
    start = time ()             # begin counting time
    zeros = 0
    while num > 0:              # with the number is within our range
        n = num
        while n > 0:
            if n % 10 is 0:     # (if it ends in zero)
                zeros += 1
            n = n // 10         # look at the next digit
        num -= 1                # look at the next number
    end = time ()               # end counting
    return zeros, end - start   

given = int(input("What number do you want to count zeros to? "))
counted, count_time = count (given)
print (f"The number of zeros written from 1 to {given} is {counted}.")
print (f"This took {count_time} seconds.")