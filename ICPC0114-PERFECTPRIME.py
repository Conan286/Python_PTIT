import math


def rev(n):
    s = ""
    while n:
        s = str(int(n % 10)) + s
        n //= 10
    return int(s)


def prime(n):
    k = int(math.sqrt(n))
    for i in range(2, k + 1):
        if n % i == 0:
            return 0
    return 1 if n > 1 else 0


def checksum(n):
    s = str(n)
    sum = 0
    for i in s:
        if i != '2' and i != '3' and i != '5' and i != '7':
            return 0
        sum += ord(i) - 48
    return 1 if prime(sum) else 0


def check(n):
    return "Yes" if (prime(n) and prime(rev(n)) and checksum(n)) else "No"


def main():
    t = int(input())
    while t:
        n = int(input())
        print(check(n))
        t -= 1


if __name__ == "__main__":
    main()
