import math


def consoduyenno(s):
    return 1 if s[0] == s[-1] else 0


def check(n):
    return "YES" if (consoduyenno(n)) else "NO"


def main():
    t = int(input())
    while t:
        n = str(input())
        print(check(n))
        t -= 1


if __name__ == "__main__":
    main()
