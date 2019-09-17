#!/usr/bin/env python3


def add_first_and_last(ints:list) -> int:

    return sum([ints[0],ints[-1]]) if len(ints) > 1 else sum(ints)


if __name__ == "__main__":
    print(add_first_and_last([]))
    print(add_first_and_last([2, 7, 4, 3]))
    print(add_first_and_last([10]))
