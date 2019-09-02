import sys
from time import sleep

hold = []
def F(n):
    if n == 0: res = 0

    elif n == 1: res = 1

    else:
        res = F(n-1) + F(n-2)
        hold.append(res)

    return res

def f(n):
    fib = [0,1]
    if n:
        for each in range(n):
            fib.append(sum(fib[::-2]))
        print(fib[-1])
    else:
        print(n)


if __name__ == "__main__":
    try:
        #print([F(x) for x in range(int(sys.argv[1]))])
        #print(F(int(sys.argv[1])))
        #f(int(sys.argv[1]))
    except KeyboardInterrupt:
        pass

