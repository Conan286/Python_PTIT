import math
import re
def main():
    t = int(input())
    while t:
        a = []
        b = []
        n = int(input())
        for i in range(n):
            x,y = map(float,input().split())
            a.append(x)
            b.append(y)
        ans = 1
        dp = [1]*500
        for i in range(n):
            dp[i]=1
            for j in range(i):
                if a[i]>a[j] and b[i]<b[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        print(max(dp))
        t -= 1

if __name__ == '__main__':
    main()