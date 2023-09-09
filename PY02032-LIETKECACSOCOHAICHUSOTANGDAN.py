import math
import re
from functools import cmp_to_key
import sys
def main():
    Set = set()
    s = str(input())
    if len(s)%2!=0: s = s[:len(s)-1]
    n = len(s)
    for i in range(0,n-1,2):
        Set.add(int(s[i:i+2]))
    a = sorted(list(Set))
    for i in a:
        print(i,end=' ')

if __name__ == '__main__':
    main()