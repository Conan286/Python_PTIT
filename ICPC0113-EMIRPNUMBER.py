import math
import re
from functools import cmp_to_key
import sys

N = 10**6+1
p = [1]*N


def rev(s):
    s = str(s)
    ans = ""
    for i in s: ans = i+ans
    return int(ans)
def sang():
    p[0] = p[1] = 0
    k = int(math.sqrt(N))+1
    for i in range (2,k):
        if p[i]:
            for j in range (i*i,N,i):
                p[j] = 0


def main():
    sang()
    t = int(input())
    while t:
        n = int(input())
        for i in range(2,n):
            if p[i]:
                k = rev(i)
                if k<n and k>i and p[k]:
                    print(i,k,end=' ')
        print()
        t -= 1

if __name__ == '__main__':
    main()