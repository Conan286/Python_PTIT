import math

def rev(n):
    n = str(n)
    ans = ""
    for i in n:
        ans = i+ans
    return int(ans)
def res(n):
    if n%7==0: return n
    cnt = 1000
    while cnt:
        n = n + rev(n)
        if n%7==0: return n
        cnt -= 1
    return -1

def main():
    t = int(input())
    while t:
        n = int(input())
        print(res(n))
        t -= 1

if __name__ == '__main__':
    main()