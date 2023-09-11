import math
import re
from functools import cmp_to_key
import sys

def main():
      a = str(input())
      b = str(input())
      s = ""
      while len(a)<len(b): a = "0"+a
      while len(b)<len(a): b = "0"+b
      n = len(a)
      cur = 0
      for i in range(n-1,0,-1):
          sum = ord(a[i])-48+ord(b[i])-48+cur
          if sum>=10:
              cur=1
              sum%=10
          else:
              cur = 0
          s = str(sum)+s
      s = str(ord(a[0])-48+ord(b[0])-48+cur)+s
      while s[0] == '0' and len(s)>1:
          s = s[1:]
      print(s)
if __name__ == '__main__':
    main()