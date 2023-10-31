import math

def ans(s,n,m):
    cnt = 0
    k = len(s)
    k = n-k
    if k==0 : return 1
    cnt = 26*(k+1)%m
    if s[0]==s[len(s)-1]: cnt-=1
    return cnt

def main():
    t = int(input())
    while t:
        n,m = map(int,input().split())
        s = str(input())
        print(ans(s,n,m))
        t -= 1


if __name__ == '__main__':
    main()