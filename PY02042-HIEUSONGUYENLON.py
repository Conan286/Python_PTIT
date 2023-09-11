import math
import re
from functools import cmp_to_key
import sys

def main():
      a = str(input())
      b = str(input())
      s = ""
      dau = ""
      while a[0]=='0' and len(a)>1: a = a[1:]
      while b[0]=='0' and len(a)>1: b = b[1:]
      while len(a)<len(b): a = "0"+a
      while len(b)<len(a): b = "0"+b
      n = len(a)
      if a<b:
            dau += "-"
            a,b = b,a

      i = n-1
      cur = 0
      while i>=0:
            k = ord(a[i])-ord(b[i])-cur
            if k<0:
                  k+=10
                  cur = 1
            else:
                  cur = 0
            s = str(k)+s
            i -= 1

      while s[0]=='0' and len(s)>1:
            s = s[1:]
      s = dau + s
      print(s)


if __name__ == '__main__':
    main()