import math
from functools import cmp_to_key

def compare(a,b):
    if mul(a)!=mul(b):
        return mul(a)-mul(b)
    return a-b

def mul(n):
    ans = 1
    while n:
        ans *= n%10
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