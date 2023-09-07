import math
from functools import cmp_to_key


def main():
    t = int(input())
    while t:
        a,b,c,d = map(int,input().split())
        s1 = complex(a,b)
        s2 = complex(c,d)
        sc = (s1+s2)*s1
        sd = (s1+s2)**2
        a = int(sc.real)
        b = int(sc.imag)
        c = int(sd.real)
        d = int(sd.imag)
        if b<0: print(a,' - ',abs(b),'i, ',sep='',end='')
        else: print(a,' + ',b,'i, ',sep='',end='')
        if d<0:print(c,' - ',abs(d),'i',sep='',end='')
        else:print(c,' + ',abs(d),'i',sep='',end='')
        print()
        t-=1

if __name__ == '__main__':
    main()