#!/usr/bin/env python3
from sys import argv


if len(argv) > 1:
    with open(argv[1], 'r') as file:
        print(file.read())
