# Roi des tris

import sys

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]    
    return i + 1


def quicksort(array_nb, low, high):
    if low < high:
        pivot = partition(array_nb, low, high)
        quicksort(array_nb, low, pivot - 1)
        quicksort(array_nb, pivot + 1, high)
        return " ".join(array_nb)
    
try:
    if len(sys.argv) < 3:
        sys.exit()
    else:
        array = sys.argv[1:]
        size = len(array) - 1
        for x in array:
            if not int(x):
                sys.exit()
        print(quicksort(array, 0, size))
except:
    print("error")
    sys.exit()