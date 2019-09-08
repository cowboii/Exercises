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


def find_and_replace(text:str , find_str:str, replace_str:str) -> str:

    word_len = len(find_str)

    while find_str in text:
        index = search(text, find_str)
        #print(f"Found word at index {index}")
        text = text[:index] + replace_str + text[index+word_len:]

    return text


if __name__ == "__main__":

    if len(argv) > 3:
        with open(argv[1], 'r') as file:
            print(find_and_replace(file.read(), *argv[2:4]))

