import math
import re
from functools import cmp_to_key
import sys
mp = {}

def main():
    n = int(input())
    a = []
    ans = 0
    for i in range(n):
        s = list(str(input()))
        coin = s.count('C')
        ans += math.comb(coin,2)
        a.append(s)
    for i in range(n):
        coin = 0
        for j in range(n):
            if  a[j][i]=='C':
                coin += 1
        ans += math.comb(coin,2)
    print(ans)


if __name__ == '__main__':
    main()