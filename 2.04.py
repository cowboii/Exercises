#!/usr/bin/env python3
from sys import argv

def search(string: str, substring: str) -> int:

    if substring not in string:
        return -1

    count = 0
    while count < (len(string)-len(substring)+1):

        if substring == string[count:count+len(substring)]:
            return count

        else:
            count += 1

if __name__ == "__main__":
    print(search(*argv[1:3]))

