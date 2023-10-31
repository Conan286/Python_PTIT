import math
import re
def main():
    n, k = map(int, input().split())
    pre = list(map(int, input().split()))
    next = list(map(int, input().split()))
    a = [[] for _ in range(n)]
    for i in range(n):
        a[i] = [pre[i], next[i]]
    a.sort(key = lambda x: (x[0] - x[1]))
    i = 0
    cnt = 0
    while i < n:
        if k:
            cnt += a[i][0]
            k -= 1
        else:
            if a[i][0] < a[i][1]: cnt += a[i][0]
            else: cnt += a[i][1]
        i += 1
    print(cnt)
if __name__ == '__main__':
    main()