#!/usr/bin/env python3
"""
module.py - an example of a Python module
"""

__counter: int = 0


def sum_list(the_list: list[int]) -> int:
    global __counter
    __counter += 1
    sum: int = 0

    for element in the_list:
        sum += element
    return sum


def prod_list(the_list: list[int]) -> int:
    global __counter
    __counter += 1
    prod: int = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("Called directly. Running tests...")
    my_list: list[int] = [i + 1 for i in range(5)]
    print(sum_list(my_list))
    print(prod_list(my_list))
