#!/usr/bin/env python3
from numbers import Number

def sum_numbers(any_list):
    return sum([x for x in any_list if isinstance(x, Number)])

if __name__ == "__main__":
    print(sum_numbers([1, 2, 3.2, 4, 5 ]))
    print(sum_numbers(["a", 1, "b", 2, [["b", 4], 2], 3]))
