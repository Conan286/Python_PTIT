import math
import re
from functools import cmp_to_key
import sys
def fee(Type,soGhe,Tt):
    if Tt=="OUT":
        return 0
    elif Type=="Xe_con":
        if soGhe=="5":
            return 10000
        if soGhe=="7":
            return 15000
    elif Type=="Xe_khach":
        if soGhe=="29":
            return 50000
        if soGhe=="45":
            return 70000
    return 20000
def main():
      t = int(input())
      mp = {}
      while t:
            Id,Type,soGhe,Tt,Day = map(str,input().split())
            if Day in mp:
                mp[Day] += fee(Type,soGhe,Tt)
            else:
                mp[Day] = fee(Type,soGhe,Tt)
            t -= 1
      for k,v in mp.items():
          print(k,v,sep=': ')

if __name__ == '__main__':
    main()