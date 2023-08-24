import math

def main():
    t = int(input())
    while t:
         n = int(input())
         m = int(input())
         print(math.gcd(n,m))
         t -= 1

if __name__ == "__main__":
    main()
