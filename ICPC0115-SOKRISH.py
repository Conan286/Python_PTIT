import math


def krish(n):
    k = n
    s = 0
    while k:
        s += math.factorial(int(k % 10))
        k //= 10
    return 1 if s == n else 0


def check(n):
    return "Yes" if (krish(n)) else "No"


def main():
    t = int(input())
    while t:
        n = int(input())
        print(check(n))
        t -= 1


if __name__ == "__main__":
    main()
