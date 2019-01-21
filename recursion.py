"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""
import time


def get_fib(position):
    if position < 0:
        return -1
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)


cache = {}


def get_fib_optimised(position):
    if position < 0:
        return -1
    if position == 0 or position == 1:
        cache[position] = position
        return position
    else:
        if not (position - 1) in cache:
            cache[position - 1] = get_fib(position - 1)

        if not (position - 2) in cache:
            cache[position - 2] = get_fib(position - 2)

        return cache[position - 1] + cache[position - 2]


start_time = time.time()
print get_fib_optimised(20)
print("--- %s seconds ---" % (time.time() - start_time))
