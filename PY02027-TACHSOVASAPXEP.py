import math
import re
from functools import cmp_to_key
import sys
n,m,y = 0,0,0
vs = [0]*(n+1)
adj = [[]]*1001


def main():
      t = int(input())
      a = []
      while t:
          s = str(input())
          n = len(s)
          i = 0
          while i<n:
              if s[i].isdigit():
                  c = 0
                  while i<n and s[i].isdigit():
                      c = c*10 + ord(s[i])-48
                      i += 1
                  a.append(c)
              else: i+=1
          t -= 1

      a.sort()
      for i in a:  print(i)
if __name__ == '__main__':
    main()