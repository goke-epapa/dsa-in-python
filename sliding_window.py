import sys

'''
Given an array of positive integers of size n.
Our aim is to calculate the maximum sum of k
consecutive elements in the array.
'''


def max_sum(a, n, k):
    sum_max = -sys.maxint

    window_sum = 0
    for i in range(0, k):
        window_sum += a[i]

    for i in range(k, n):
        window_sum += a[i] - a[i - k]

        if window_sum > sum_max:
            sum_max = window_sum

    return sum_max

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print max_sum(arr, len(arr), 3)



