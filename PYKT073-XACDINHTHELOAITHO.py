import math
from functools import cmp_to_key


def main():
    n = int(input())
    a = []
    cnt = 0
    while n:
        l = list(map(str,input().split()))
        b = len(l)
        if b==7: cnt += 1
        else: cnt = 0
        if (b==7) and (len(a)==0 or a[-1]!=2 ):
            a.append(2)
        elif (b!=7) and(len(a)==0 or (a[-1]==2)):
            a.append(1)
        if cnt%4==0 and cnt>4: a.append(2)
        n-=1
    print(len(a))
    for item in a:
        print(item)

if __name__ == '__main__':
    main()