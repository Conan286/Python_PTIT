# 5
# 18 27 16 22 6
import math
import re

def check(a,i):
    for j in range(len(a)):
        if a[j]//i == a[j]//(i+1):
            return 0
    return 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    k = min(a)
    sum = 0
    for i in range(k,0,-1):
        if(check(a,i)):
            for j in range(n):
                sum += a[j]//(i+1)+1
            break
    print(sum)

if __name__ =='__main__':
    main()