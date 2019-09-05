from sys import argv


def case(string):
    hold = []
    for each in string:
        current = ord(each)
        if current > 90:
            hold.append(chr(current-32))
        else:
            hold.append(each)
    return "".join(hold)


if __name__ == "__main__":
    print(case(argv[1]))
