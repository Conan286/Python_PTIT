import math
import re
from functools import cmp_to_key
import sys

def main():
        n,m = map(int,input().split())
        a = list(map(int,input().split()))
        freg = {}
        for i in a:
            if i in freg:
                freg[i] += 1
            else:
                freg[i]  = 1
        mp = list(set(freg.values()))
        mp.sort()

        if len(mp)<2: print("NONE")
        else:
            k = mp[-2]
            for i in range(1,m+1):
                if freg[i]==k:
                    print(i)
                    break



if __name__ == '__main__':
    main()