import math
from functools import cmp_to_key


def main():
    t = int(input())
    while t:
       n,m = map(int,input().split())
       a = list(map(int,input().split()))
       maxOfArray = max(a)
       a.insert(a.index(maxOfArray),m)
       neg = list(filter(lambda x:x<0,a))
       pos = list(filter(lambda x:x>=0,a))
       new = neg + pos
       for item in new:
           print(item,end=' ')
       print()
       t -= 1

if __name__ == '__main__':
    main()