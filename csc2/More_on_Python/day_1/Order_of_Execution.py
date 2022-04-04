# Example of Order of Execution

def min (a,b):                                          #4th    4th
    if a < b:                                           #5th    5th
        return                                          #6th
    else:                                               #       6th
        return b                                        #       7th


def max (a,b):                                          
    if a > b:                                           #8th    9th
        return a                                        #       10th
    else:                                               #9th
        return b                                        #10th


num1 = int(input("Enter an integer: "))                 #1st    1st

num2 = int(input("Enter another integer: "))            #2nd    2nd

print (f"The smaller integer is {min (num1, num2)}.")   #3rd    3rd

print (f"The larger integer is {max (num1, num2)}.")    #7th    8th
