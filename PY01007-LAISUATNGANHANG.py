import math


def main():
        t = int(input())
        while t:
            a,b,c = map(float,input().split())
            n = 0
            while a<c:
                a += a*b/100.0
                n += 1
            print(n)
            t -= 1

if __name__ == "__main__":
    main()