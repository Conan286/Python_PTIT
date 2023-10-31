from math import *
from functools import cmp_to_key
import re

def pivot(a):
    l = []
    r = []
    n = len(a)
    cnt = 0
    il,vl,ir,vr = 0,a[0],n-1,a[n-1]
    while il<n:
        vl = max(vl,a[il])
        l.append(vl)
        il+=1
    while ir>=0:
        vr = min(vr,a[ir])
        r.append(vr)
        ir -= 1
    r.reverse()
    if n>1 and a[0]<r[1]: cnt+=1
    for i in range(1,n-1):
        if a[i]>=l[i] and a[i]<r[i+1]:
            cnt += 1
    if n>1 and a[n-1]>=l[n-1]: cnt+=1
    return cnt


def main():
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int,input().split()))
        print(pivot(a))
        t -= 1

if __name__ == '__main__':
    main()