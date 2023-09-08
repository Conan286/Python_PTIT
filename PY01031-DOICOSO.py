import math

def doiCoSo(N,b):
    ans = ""
    while N:
        k = N%b
        if k<10: ans=str(k)+ans
        else: ans=chr(k+55)+ans
        N //= b
    return ans

def main():
    t = int(input())
    while t:
        N,b = map(int,input().split())
        print(doiCoSo(N,b))
        t -= 1

if __name__ == '__main__':
    main()