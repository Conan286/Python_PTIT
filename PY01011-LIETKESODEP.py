import math
from functools import cmp_to_key

N = 888889
p = []
def soDep(n):
    n = str(n)
    if len(n)%2!=0: return 0
    l,r = 0,len(n)-1
    while l<r:
        if n[l]!=n[r] or (ord(n[l])-48)%2!=0:
            return 0
        l+=1
        r-=1
    return 1
def sang():
    for i in range(N):
        if soDep(i):
            p.append(i)


def main():
   sang()
   t = int(input())
   while t:
      n = int(input())
      for i in p:
          if i<n:
              print(i,end=' ')
          else: break
      print()
      t -= 1

if __name__ == '__main__':
    main()