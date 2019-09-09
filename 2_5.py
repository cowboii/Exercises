#!/usr/bin/env python3
from sys import argv


def get_char(string: str, index: str) -> str:

    if abs(index) > len(string):
        return "Invalid position"

    return string[index]


if __name__ == "__main__":
    print(get_char(argv[1],int(argv[2])))
