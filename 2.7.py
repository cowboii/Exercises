#!/usr/bin/env python3
from sys import argv


def check_palindrome(string: str) -> bool:

    return string == string[::-1]


def main():

    while True:
        word = input("Write a word: ")

        if word.lower() in ["quit","exit"]:
            break

        if check_palindrome(word.lower()):
            print(f"{word} is a palindrome\n")

        else:
            print(f"{word} is not a palindrome\n")

    print("Exiting ...")

if __name__ == "__main__":
    main()
