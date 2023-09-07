import math
from functools import cmp_to_key

def compare(a,b):
    if sum(a)!=sum(b):
        return sum(a)-sum(b)
    return a-b

def sum(n):
    ans = 0
    while n:
        ans += n%10
        n //= 10
    return ans

def main():
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int,input().split()))
        a.sort(key=cmp_to_key(compare))
        for i in a: print(i,end=' ')
        print()
        t -= 1

if __name__ == '__main__':
    main()