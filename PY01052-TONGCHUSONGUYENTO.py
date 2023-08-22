import math
def prime(n):
    k = int(math.sqrt(n))
    for i in range(2,k+1):
        if n % i == 0:
            return 0
    return 1 if n>1 else 0
def sum(s):
    ans = 0
    for i in s:
        ans+=ord(i)-48
    return ans
def check(s):
    return "YES" if prime(sum(s)) else "NO"

def main():
        t = int(input())
        while t>0:
            s = str(input())
            print(check(s))
            t -=1

if __name__ == '__main__':
    main()
