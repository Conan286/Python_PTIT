import math
import re
from functools import cmp_to_key
freg = {}
def cmp(s1,s2):
    if freg[s1]!=freg[s2]:
        return freg[s2]-freg[s1]
    return 1 if s1>s2 else -1
def main():
    newset = set()
    t = int(input())
    while t:
        s = str(input().lower())
        ss = re.sub(r'[^a-zA-Z0-9]',' ',s)
        arr_string = list(ss.split())
        for i in arr_string:
            if i in freg:
                freg[i]+=1
            else:
                freg[i] = 1
                newset.add(i)
        t -= 1
    ne = list(newset)
    ne.sort(key=cmp_to_key(cmp))
    for item in ne:
        print(item,freg[item])
if __name__ == '__main__':
    main()