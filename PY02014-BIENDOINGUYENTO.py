import math
from functools import cmp_to_key

N = 10008
p = [1]*N
nt = []
l = [0]*N
r = [0]*N
st = [0]*N
def sang():
    p[0] = p[1] = 0
    k = int(math.sqrt(N))+1
    for i in range(2,k):
        if p[i]:
            for j in range(i*i,N,i):
                p[j] = 0
    val = 3
    for i in range(4,N):
        if p[i]: val = i; l[i]=i
        else: l[i] = val
    val = 10007
    for i in range(N-2,-1,-1):
        if p[i]: val = i; r[i] = i
        else: r[i] = val
    st[0] = 2
    st[1] = 1
    for i in range(2,N):
        if p[i]: continue
        else: st[i] = min(i-l[i],r[i]-i)

def main():
   sang()
   n = int(input())
   a = list(map(int,input().split()))
   b = list(map(lambda i: st[i],a))
   print(max(b))

if __name__ == '__main__':
    main()