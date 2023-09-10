import math
import re
from functools import cmp_to_key
import sys
def ans(a,n,k):
    for i in range(1,n):
        if math.gcd(a[i],a[i-1])==k:
            return 2
    return -1

def main():
      s = str(input())
      if len(s)%2!=0:
          s = s[:len(s)-1]
      mp = {}
      n = len(s)
      for i in range(0,n,2):
          k = int(s[i:i+2])
          if k in mp: mp[k] += 1
          else:
              mp[k] = 1
      for key,val in mp.items():
          print(key,val)

if __name__ == '__main__':
    main()