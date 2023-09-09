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
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(list(filter(lambda i: prime(i),a)))
    id = []
    for i in a:
        if prime(i): id.append(1)
        else: id.append(0)
    cnt = 0
    for i in a:
        if prime(i):
            print(b[cnt],end=' ')
            cnt += 1
        else: print(i,end=' ')

if __name__ == '__main__':
    main()