import math
import re
from functools import cmp_to_key
import sys

def main():
      t = int(input())
      while t:
          m,n,k = map(int,input().split())
          a = list(map(int,input().split()))
          b = list(map(int,input().split()))
          c = list(map(int,input().split()))
          i,j,h = 0,0,0
          check = 0
          while i<m and j<n and h<k:
              if a[i] == b[j] and b[j] == c[h]:
                  print(a[i],end = ' ')
                  check = 1
                  i += 1
                  j += 1
                  h += 1
              elif a[i]<b[j]:
                  i += 1
              elif b[j]<c[h]:
                  j += 1
              else:
                  h += 1
          if(check==0): print("NO",end='')
          print()
          t -= 1
if __name__ == '__main__':
    main()