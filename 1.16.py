#!/usr/bin/env python3
from sys import argv


def unit(int_num:int) -> int:
    return int(str(int_num)[-1])

def ten(int_num:int) -> int:
    return int(str(int_num)[-2])

def swap_units_and_tens(int_num:int) -> int:
    return str(int_num)[:-2] + str(unit(int_num)) + str(ten(int_num))


if __name__ == "__main__":
    print(swap_units_and_tens(int(argv[1])))
