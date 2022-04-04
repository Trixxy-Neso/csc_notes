####################################################################
####    Name:   Josephine Rei Sale                              ####
####    Date:   2 - 19 - 2022                                   ####
####    Desc:   Using Sort_Comp and plot, graph comps & swaps   ####
####################################################################

from plot import plot

# creates the list
def getList():
	return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bub_sort (lisst):
    n = len (lisst)
    num_1 = 0
    num_2 = 0
    for i in range (1, n):
        for j in range (1, n - i + 1):
            num_1 += 1
            if lisst [j] < lisst [j - 1]:
                num = lisst [j - 1]
                lisst [j - 1] = lisst [j]
                lisst [j] = num
                num_2 += 1
    return (num_1, num_2)

# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def opt_bub_sort (lisst):
    n = len (lisst)
    end = False
    num_1 = 0
    num_2 = 0
    for i in range (1, n):
        switch = False
        for j in range (1, n - i + 1):
            num_1 += 1
            if lisst [j] < lisst [j - 1]:
                num = lisst [j - 1]
                lisst [j - 1] = lisst [j]
                lisst [j] = num
                num_2 += 1
                switch = True
        if switch == False:
            return (num_1,num_2)
    return (num_1, num_2)


# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selection_sort(lisst):
    num_1 = 0
    num_2 = 0
    for i in range(len(lisst) - 1):  
        min_index = i
        for j in range(i + 1, len(lisst)):
            num_1 += 1
            if lisst[j] < lisst[min_index]:
                min_index = j
        if lisst [i] != lisst [min_index]:
            num_2 += 1
        lisst[i], lisst[min_index] = lisst[min_index], lisst[i]
    return (num_1, num_2)


# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def ins_sort (lisst):
    n = len (lisst)
    i = 1
    num_1 = 0
    num_2 = 0
    while (i < n):
        num_1 += 1
        if (lisst[i - 1] > lisst[i]):
            temp = lisst[i]
            j = i - 1
            num_2 += 1
            num_1 += 1
            while (j >= 0 and lisst[j] > temp):
                lisst[j + 1] = lisst[j]
                lisst[j] = temp
                j -= 1
                num_1 += 1
            i += 1
            num_2 += 1
        else:
            num_1 += 1
            i += 1
    return (num_1, num_2)

# the main part of the program
list_1 = getList ()
list_2 = getList ()
list_3 = getList ()
list_4 = getList ()


bubble = bub_sort (list_1)

optimised = opt_bub_sort (list_2)

selection = selection_sort (list_3)

insertion = ins_sort (list_4)

plot(bubble, optimised, selection, insertion)