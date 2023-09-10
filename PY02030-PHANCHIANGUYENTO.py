import math
import re
from functools import cmp_to_key
import sys
def prime(n):
    if n<2: return 0
    k = int(math.sqrt(n))+1
    for i in range(2,k):
        if n%i==0:
            return 0
    return 1
def main():
        n = (int,input())
        a = list(map(int,input().split()))
        b = []
        s = []
        s.append(a[0])
        for i in a:
            if i in b: continue
            b.append(i)
        m = len(b)
        for i in range(1,m):
            s.append(b[i]+s[i-1])
        check = 0
        for i in range(0,m):
            if prime(s[i]) and prime(s[-1]-s[i]):
                print(i)
                check = 1
                break
        if check==0:
            print("NOT FOUND")


if __name__ == '__main__':
    main()