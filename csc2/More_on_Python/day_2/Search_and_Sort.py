# sequential search
def sequential_max (the_list):
    current_index = 0
    max_value = the_list [0]        # start max is whatever is first

    while current_index < len (the_list) - 1:       # go through list
        current_index += 1
        if the_list [current_index] > max_value:
            max_value = the_list [current_index]

    return max_value

def sequential_min (the_list):
    current_index = 0
    min_value = the_list [0]

    while current_index < len (the_list) - 1:
        current_index += 1
        if the_list [current_index] < min_value:
            min_value = the_list [current_index]

    return min_value


def sequential_equal (search_val, the_list):
    current_index = 0
    found = False
    while current_index < len (the_list) and found == False:
        if the_list [current_index] = search_val:
            found = True
        else:
            pass



def binary_search (search_val, the_list):
    left_index = 0
    right_index = -1
    found = False
    while left_index <= right_index and found != True:
        mid_index = (left_index + right_index) // 2
        if the_list [mid_index] == search_val:
            found = True
        elif the_list [mid_index] < search_val:
            left_index = mid_index
        else:
            right_index = mid_index



# bubble
def bub_sort (lisst):
    n = len (lisst)
    for i in range (1, n):
        for j in range (1, n - i + 1):
            if lisst [j] < lisst [j - 1]:
                num = lisst [j - 1]
                lisst [j - 1] = lisst [j]
                lisst [j] = num
    return (lisst)

