my_string = "hEllo WorLD"
my_other = "hello"

#capitalize returns string w/ first letter capitol, all others lower
print (my_string.capitalize())

#find returns first index of defined substring (or -1)
print (my_string.find('W'))
print ()

#determining existense of numerical
val = "094"
print (val.isnumeric())
print (val.isdecimal())
print (val.isdigit())
print ()

#other
all_caps = 'WHATEVER THIS IS'
print (all_caps.lower())
print (all_caps.split('E'))
print ("76".zfill(6))

print ("        hii     ".strip())
print ("hello".upper())
print ("mumbo".replace('m','w'))