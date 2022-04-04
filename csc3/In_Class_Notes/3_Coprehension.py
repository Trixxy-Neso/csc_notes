# List Comprehension
a_list = [2*x for x in range (0,10)]
print (a_list)

list_evens = [x for x in range (0,10) if x%2 ==0]
print (list_evens)

nesting = [(i, j) for i in range (0,2) for j in range (0,5)]
print (nesting)

more = [(i,j) for i in range (0,2) for j in range (0,5) if (i + j) % 2 == 0]
print (more)

[print ('hello') for i in range (10)]