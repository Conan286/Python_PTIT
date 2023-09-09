
import math
import re
from functools import cmp_to_key
import sys
freg = {}
def cmp(s1,s2):
    if freg[s1]!=freg[s2]:
        return freg[s2]-freg[s1]
    return 1 if s1>s2 else -1
def main():
    Set = set()
    n,k = map(int,input().split())
    while n:
        s1 = str(input().lower())
        s  = list(re.sub(r'[^0-9A-Za-z]',' ',s1).split())
        for i in s:
            if i in freg:
                freg[i] += 1
            else:
                freg[i]  = 1
                Set.add(i)
        n -= 1
    myList = list(filter(lambda i: freg[i]>=k,Set))
    myList.sort(key = cmp_to_key(cmp))
    for item in myList:
        print(item,freg[item])

if __name__ == '__main__':
    main()