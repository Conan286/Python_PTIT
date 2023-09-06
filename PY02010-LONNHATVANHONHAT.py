import math
from functools import cmp_to_key

def main():
    while 1:
        n = int(input())
        if n==0: break
        new = set()
        for i in range(n):
            new.add(int(input()))
        a = min(new)
        b = max(new)
        if a==b : print("BANG NHAU")
        else: print(a,b)


if __name__ == '__main__':
    main()
