import math


def somayman(s):
    cnt = 0
    for i in s:
        if i!='4' and i!='7':
            return 0
    return 1


def check(n):
    return "YES" if (somayman(n)) else "NO"


def main():
    t = int(input())
    while t:
         n = str(input())
         print(check(n))
         t -= 1


if __name__ == "__main__":
    main()
