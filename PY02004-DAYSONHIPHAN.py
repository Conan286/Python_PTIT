import math
import re
from functools import cmp_to_key
import sys

def main():
        n = int(input())
        cnt = 0
        a = list(map(int,input().split()))
        for i in range(1,n):
            if a[i]!=a[i-1]:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()