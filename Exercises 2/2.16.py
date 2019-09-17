#!/usr/bin/env python3


def sum_last_digits(int_list:list) -> int:

    return sum([int(str(x)[-1]) for x in int_list])


if __name__ == "__main__":
    print(sum_last_digits([123,23,541,2,1]))
    print(sum_last_digits([1,2,10]))
