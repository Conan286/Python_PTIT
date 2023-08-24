import math

def mul(n):
    t = 1
    while n:
        k = int(n%10)
        if k!=0:
           t *= k
        n //= 10
    return t

def main():
    t = int(input())
    while t:
         n = int(input())
         print(mul(n))
         t -= 1

if __name__ == "__main__":
    main()
