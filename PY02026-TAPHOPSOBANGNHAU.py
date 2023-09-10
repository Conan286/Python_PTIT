import math
import re
from functools import cmp_to_key
import sys

def main():
        n,m = map(int,input().split())
        a = set(map(int,input().split()))
        b = set(map(int,input().split()))
        if a==b:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()