import math

def coso(n,b):
    ans =""
    while n:
        k = int(n%b)
        if k<10:
            ans = str(k) + ans
        else:
            ans = chr(k+55) + ans
        n//=b
    return ans


def main():
        t = int(input())
        while t:
            n,b = map(int,input().split())
            print(coso(n,b))
            t -= 1

if __name__ == "__main__":
    main()