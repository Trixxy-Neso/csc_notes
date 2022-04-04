######################################################################################################################
# Name: Josephine Rei Sale
# Date: 12/16/2021 - 12/17/2021 (Sorry that it's late...)
# Description: A function to compare sorting functions.
######################################################################################################################

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
    return (lisst, num_1, num_2)

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
            return (lisst, num_1,num_2)
    return (lisst, num_1, num_2)


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
    return (lisst, num_1, num_2)


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
    return (lisst, num_1, num_2)

# the main part of the program
list_1 = getList ()
list_2 = getList ()
list_3 = getList ()
list_4 = getList ()

print (f"The List: {list_1}")
bub_sorted, bub_comp, bub_switch = bub_sort (list_1)
print (f"After bubble sort: {bub_sorted}\n{bub_comp} comparisons; {bub_switch} swaps\n")

print (f"The List: {list_2}")
opt_bub_sorted, opt_bub_comp, opt_bub_switch = opt_bub_sort (list_2)
print (f"After optimised bubble sort: {opt_bub_sorted}\n{opt_bub_comp} comparisons; {opt_bub_switch} swaps\n")

print (f"The List: {list_3}")
sel_sorted, sel_comp, sel_switch = selection_sort (list_3)
print (f"After selection sort: {sel_sorted}\n{sel_comp} comparisons; {sel_switch} swaps\n")

print (f"The List: {list_4}")
ins_sorted, ins_comp, ins_switch = ins_sort (list_4)
print (f"After insertion sort: {ins_sorted}\n{ins_comp} comparisons; {ins_switch} swaps")