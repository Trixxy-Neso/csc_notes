# Scope = region of code a variable is excesable in
    # Global Variables accessible everywhere
    # Local Variabes defined in a regional context
    # Shadowing when local variable covers global variable


a = 10

def my_func (x):
    a = 11
    b = 5
    x *= 2
    print(f"In my_func: a = {a}, b = {b}, x={x}")

b = 20
my_func (b)

print (f"In the main program: a = {a}, b = {b}")

def jared():
    global a
    a *= 1.5
    print (f"in jared: a = {a}, b = {b}")

jared ()
print (f"In the main program: a = {a}, b = {b}")


# This is terible practice, BTW