import math
import re
from functools import cmp_to_key
import sys
def sumString(s):
    sum = 0
    for i in s:
        sum += ord(i)-65
    return sum
def Rotate(s,k):
    ans = ""
    for i in s: ans += chr((ord(i)-65+k)%26+65)
    return ans

def Merge(s1,s2):
    ans = ""
    n = len(s1)
    for i in range(n):
        k = ord(s2[i])-65
        ans+=chr((ord(s1[i])-65+k)%26+65)
    return ans
def main():
    t = int(input())
    while t:
        s = str(input())
        divide = int(len(s)/2)
        s1,s2=Rotate(s[:divide],sumString(s[:divide])),Rotate(s[divide:],sumString(s[divide:]))
        print(Merge(s1,s2))
        t -= 1

if __name__ == '__main__':
    main()