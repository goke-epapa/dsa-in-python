"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    pivot = 0
    store_index = pivot + 1

    sorted_index = 0
    rightmost_index = len(array) - 1
    while rightmost_index != 0:
        pivot = sorted_index
        for i in range(pivot + 1, len(array)):
            if array[i] < array[pivot]:
                swap(array, i, store_index)
                store_index += 1
        swap(array, pivot, store_index - 1)
        rightmost_index = store_index - 1
    return array


def swap(array, i, j):
    temp = array[j]
    array[j] = array[j + 1]
    array[j + 1] = array[i]
    array[i] = temp


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
