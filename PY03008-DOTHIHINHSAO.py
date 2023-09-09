import math
import re
from functools import cmp_to_key
import sys
mp = {}

def main():
    n = int(input())
    Set = set()
    k = 0
    for i in range(n-1):
        u,v = map(int,input().split())
        Set.add(u)
        Set.add(v)
        if u in mp: mp[u] += 1
        else: mp[u] = 1
        if v in mp: mp[v] += 1
        else: mp[v] = 1
        k = max(k,mp[u],mp[v])
    if k==n-1 and len(Set)==n:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    main()