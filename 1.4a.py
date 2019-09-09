from datetime import timedelta

while True:
    try:
        minutes, seconds = map(int, input("Please give me some time in the "
                "format of MM:SS\n").split(":"))

        time = timedelta(minutes=minutes, seconds=seconds)
        break
    except ValueError:
        print("Invalid input. Try again")

print("Det går {} sekunder på {} min och {} sek".format(
        time.total_seconds(),
        *str(time).split(':')[1:]
        )
    )
