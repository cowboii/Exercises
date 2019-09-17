#!/usr/bin/env python3
from sys import argv


def add_numbers_in_list(num_list:list) -> int:
    num = 0

    for x in num_list:
        num += int(x)

    return num


if __name__ == "__main__":

    print(add_numbers_in_list(argv[1:]))
