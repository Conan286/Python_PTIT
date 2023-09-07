import math
from functools import cmp_to_key


def kytu(n,k):
    if n==1: return 'A'
    l = pow(2,n-1)
    if k==l: return chr(ord('A')+n-1)
    elif k<l: return kytu(n-1,k)
    return kytu(n-1,k-l)


def main():
    t = int(input())
    while t:
       n,k = map(int,input().split())
       print(kytu(n,k))
       t -= 1

if __name__ == '__main__':
    main()