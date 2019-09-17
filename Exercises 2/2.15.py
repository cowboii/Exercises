#!/usr/bin/env python3

def find_letter(char, lst):
    return True if char in lst else False


if __name__ == "__main__":
    print(find_letter("u", ["h", "o", "u", "s", "e"]))
    print(find_letter("b", ["c", "a", "r"]))
