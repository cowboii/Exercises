#!/usr/bin/env python3
from sys import argv


def mtable(value:int=10) -> str:

    table = list()
    hold = [x for x in range(1,int(value)+1)]

    max_len = len(str(hold[-1] * hold[-1]))

    for num in hold:
        temp = list()
        for x in hold:
            current = str(x * num)
            temp.append(f"{current:>{max_len}}")
        table.append(" ".join(temp))

    return "\n".join(table)


def fwrite(string:str, name:str="mtable.txt") -> None:

        with open(name, 'w') as file:
            file.write(string)


if __name__ == "__main__":

    if len(argv) > 2:
        fwrite(mtable(argv[1]), argv[2])
    else:
        fwrite(mtable(argv[1]))




