#!/usr/bin/env python3
"""
module.py - an example of a Python module
"""

__counter: int = 0


def sum_list(the_list: list[int]) -> int:
    """
    requires
        nothing
    returns
        the sum of the_list's elements
    """
    global __counter
    __counter += 1
    sum: int = 0

    for element in the_list:
        sum += element
    return sum


def prod_list(the_list: list[int]) -> int:
    """
    requires
        nothing
    returns
        the product of the_list's elements
    """
    global __counter
    __counter += 1
    prod: int = 1

    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    my_list: list[int]

    print("Called directly. Running tests...")
    my_list = [i for i in range(1, 6)]
    print(sum_list(my_list))
    print(prod_list(my_list))
