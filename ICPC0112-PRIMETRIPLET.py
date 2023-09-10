import math
import re
from functools import cmp_to_key
import sys

N = 10**6+1
p = [1]*N
tri = [0]*N
def sang():
    p[0] = p[1] = 0
    k = int(math.sqrt(N))
    for i in range (2,k):
        if p[i]:
            for j in range (i*i,N,i):
                p[j] = 0
    for i in range (2,N-6):
        if p[i] and (p[i+2] or p[i+4]) and p[i+6]:
            p[i] = 1
        else: p[i] = 0
    cur = 0
    for i in range(2,N):
        tri[i] = cur
        if p[i]: cur += 1


def main():
    sang()
    t = int(input())
    while t:
        i = int(input())
        i = (i-6) if i>=6 else 0
        print(tri[i])
        t -= 1

if __name__ == '__main__':
    main()