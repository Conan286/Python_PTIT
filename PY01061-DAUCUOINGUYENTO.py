import math
def prime(n):
    if n<2: return 0
    k = int(math.sqrt(n))
    for i in range(2,k+1):
        if n % i ==0:
            return 0
    return 1
def check(s):
    dau = int(s[:3])
    cuoi = int(s[-3:])
    return "YES" if (prime(dau) and prime(cuoi)) else "NO"

def main():
    t = int(input())
    while(t>0):
        s = str(input())
        print(check(s))
        t -= 1

if __name__ == '__main__':
    main()
