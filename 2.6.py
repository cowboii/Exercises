#!/usr/bin/env python3
from sys import argv


def count_vowels(string: str) -> int:

    count = 0

    for each in string:

        if each in "aeoiuy":
            count += 1

    return count

if __name__ == "__main__":
    print(count_vowels(argv[1]))
