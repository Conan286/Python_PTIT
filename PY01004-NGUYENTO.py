import math
from functools import cmp_to_key

N = 10001
p = [1]*N
def sang():
    p[0] = p[1] = 0
    k = int(math.sqrt(N))+1
    for i in range(2,k):
        if p[i]:
            for j in range(i*i,N,i):
                p[j] = 0


def main():
   sang()
   t = int(input())
   while t:
       n = int(input())
       cnt = 0
       for i in range(1,n):
           if math.gcd(i,n) == 1:
               cnt += 1
       if (p[cnt]): print("YES")
       else: print("NO")
       t -= 1

if __name__ == '__main__':
    main()