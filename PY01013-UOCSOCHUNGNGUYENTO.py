import math


def sums(n):
    s = 0
    while n > 0:
        s += int(n % 10)
        n /= 10
    return s


def isPrime(n):
    if n < 2:
        return 0
    k = int(math.sqrt(n))
    for i in range(2, k+1):
        if n % i == 0:
            return 0
    return 1


def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a % b)


def main():
    t = int(input())
    while t > 0:
        a, b = map(int, input().split())
        if(isPrime(sums(gcd(a,b)))==1) :
            print("YES")
        else:
            print("NO")
        t -= 1


if __name__ == '__main__':
    main()
