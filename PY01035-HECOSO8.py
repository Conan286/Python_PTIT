import math
import re
from functools import cmp_to_key
import sys

def He10(s):
    a = 0
    n = len(s)
    for i in range(n):
        a += (ord(s[i])-48)*(2**(n-i-1))
    return str(a)
def He8(s):
    n = len(s)
    ans = ""
    for i in range(0,n-2,3):
        ans+=He10(s[i:i+3])
    return ans
def main():
    s = str(input())
    while len(s)%3!=0:
        s = "0"+s
    print(He8(s))

if __name__ == '__main__':
    main()