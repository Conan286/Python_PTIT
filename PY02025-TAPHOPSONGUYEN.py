import math
import re
from functools import cmp_to_key
import sys
mp = {}
def Print(a):
    a.sort()
    for i in a:
        print(i,end=' ')
    print()

def main():
    n,m = map(int,input().split())
    a = set(map(int,input().split()))
    b = set(map(int,input().split()))
    c = list(filter(lambda i: i in b,a))
    d = list(filter(lambda i: i not in b,a))
    e = list(filter(lambda i: i not in a,b))
    Print(c)
    Print(d)
    Print(e)


if __name__ == '__main__':
    main()