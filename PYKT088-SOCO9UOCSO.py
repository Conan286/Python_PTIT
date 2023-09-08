import math
from functools import cmp_to_key
MM = 10**9
N = int(math.sqrt(10**9))+1
p = [1]*N
a = []
b = []
def sang():
    k = int(math.sqrt(N))+1
    for i in range(2,k):
        if p[i]:
            for j in range (i*i,N,i):
                p[j] = 0
    for i in range(2,N):
        if p[i]:
            a.append(i*i)
    for i in range(2,14):
        if p[i]:
            b.append(i**8)
    n = len(a)
    for i in range(n):
        for j in range(i+1,n,1):
            kk = a[i]*a[j]
            if kk>MM: break
            else : b.append(kk)
    b.sort()

def main():
    sang()
    n = int(input())
    ans = 0
    for i in range(len(b)):
        if b[i]>n:
            ans = i
            break
    print(ans)


if __name__ == '__main__':
    main()