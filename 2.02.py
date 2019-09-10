from sys import argv


def count_e(string) -> str:

    count = 0

    for each in string:
        if each == "e":
            count += 1

    return count


if __name__ == "__main__":
    print(f"Det finns {count_e(argv[1])} \"e\" i order {argv[1]}.")
