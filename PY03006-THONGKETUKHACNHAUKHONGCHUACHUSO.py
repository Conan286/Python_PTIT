import math
import re
from functools import cmp_to_key
import sys
mp = {}
def cmp(s1,s2):
    if mp[s1]!=mp[s2] :
        return mp[s2]-mp[s1]
    return 1 if s1>s2 else -1

def reset(s):
    ans = ""
    for i in s:
        if i.isdigit():
            continue
        ans += i
    if len(ans)<1: return "WRONG"
    return ans

def main():
    Set = set()
    n = int(input())
    while n:
        string = str(input().lower())
        s = list(re.sub(r'[^0-9A-Za-z]',' ',string).split())
        for w in s:
            w = reset(w)
            if(w!="WRONG"):
                if w in mp:
                    mp[w] += 1
                else:
                    mp[w]  = 1
                    Set.add(w)
        n -= 1

    myList = list(Set)
    myList.sort(key=cmp_to_key(cmp))
    for word in myList:
        print(word,mp[word])

if __name__ == '__main__':
    main()