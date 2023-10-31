import math
import re
import collections

def main():
    t = int(input())
    for _ in range(t):
        n, m, l = [int(x) for x in input().split()]
        lst = list()
        a = [[0]*(m+1)]*(n+1)
        answer = [[0] * (m+1)]
        for i in range(n):
            d = [int(x) for x in input().split()]
            k = [0]
            tmp = 0
            for j in range(m):
                tmp = tmp + d[j]
                a[i + 1][j + 1] = a[i][j + 1] + tmp
                k.append(a[i + 1][j + 1])
            answer.append(k)
        for i in range(l, n+1):
            for j in range(l, m+1):
                print((answer[i][j] - answer[i][j-l] - answer[i-l][j] + answer[i-l][j-l]) // (l*l), end = " ")
            print()

if __name__ =='__main__':
    main()