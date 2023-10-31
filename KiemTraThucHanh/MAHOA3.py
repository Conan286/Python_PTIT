import math
import os
import re

def sum(s):
    ans = 0
    for i in s:
        ans += ord(i)-65
    return ans
def rot(s,k):
    ans = ""
    for i in s:
        ans += chr((ord(i)-65+k)%26 + 65)
    return ans
def main():
    t = int(input())
    while t:
        s = str(input())
        n = int(len(s)/2)
        s1 = s[:n]
        s2 = s[n:]
        k1 = sum(s1)
        k2 = sum(s2)

        s1 = rot(s1,k1)
        s2 = rot(s2,k2)
        ans = ""
        for i in range(len(s1)):
            ans += chr((ord(s1[i])-65+sum(s2[i]))%26 + 65)
        print(ans)
        t -= 1
if __name__ == '__main__':
    main()
# 3
# EWPGAJRB
# BB
# TPQJDRJWSQXGRRIPXFMINTELHBJA