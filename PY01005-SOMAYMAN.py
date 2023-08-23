import math


def somayman(s):
    cnt = 0
    for i in s:
        if i=='4' or i=='7':
            cnt += 1
    return 1 if (cnt==4 or cnt==7) else 0


def check(n):
    return "YES" if (somayman(n)) else "NO"


def main():
      n = str(input())
      print(check(n))


if __name__ == "__main__":
    main()
