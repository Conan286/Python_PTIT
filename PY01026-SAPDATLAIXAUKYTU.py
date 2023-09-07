import math
from functools import cmp_to_key

def main():
    t = int(input())
    for i in range(1,t+1):
        s1 = str(input())
        s2 = str(input())
        l1 = (sorted(list(s1)))
        l2 = (sorted(list(s2)))
        print("Test ",i,": ",sep='',end='')
        if(l1==l2): print("YES")
        else: print("NO")


if __name__ == '__main__':
    main()