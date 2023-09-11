import math
import re
from functools import cmp_to_key
import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))
    mp = {}
    for i in range(n):
        val = 0
        key = a[i]
        if key in mp: continue
        for j in range(n):
            if i!=j:
                val += abs(a[i]-a[j])
        mp[key] = val
    listValue = list(mp.values())
    listValue.sort()
    for k,v in mp.items():
        if v==listValue[0]:
            print(v,k)
            break
if __name__ == '__main__':
    main()