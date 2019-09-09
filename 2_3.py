from sys import argv


def count_char(string: str, char: str) -> str:

    count = 0

    for each in string:
        if each == char:
            count += 1

    return count


if __name__ == "__main__":
    print(f"Det finns {count_char(*argv[1:3])} \"{argv[2]}\" i order {argv[1]}.")
