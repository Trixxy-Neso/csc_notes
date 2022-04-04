# and, or, and not: Logical Opersators
    # a and b returns a if a is false, otherwise b
    # a or b returns b if a is false, otherwise a 
    # b not a returns false if a is true, otherwise true

a = True
b = False

print (f"a and b is {a and b}")
print (f"a or b is {a or b}")
print (f"not a is {not a}")

# truthness of numbers
print (True == 1)       #True
print (False == 0)      #True
print (True == 5)       #False
print (True == bool(5)) #True

# membership opperators: in & not in
print (5 in [1, 2, 3, 4, 5])
print (5 not in [1, 2, 3, 4, 5])