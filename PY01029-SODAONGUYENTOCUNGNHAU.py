import math
def gcd(a,b):
    return b if (a%b==0) else gcd(b,a%b)

def rev(s):
    ans = ''
    for i in s:
        ans = i+ans
    return ans
def check(s):
    a = int(s)
    b = int(rev(s))
    return "YES" if gcd(a,b)==1 else "NO"

def main():
    t = int(input())
    while(t>0):
        s = str(input())
        print(check(s))
        t -= 1

if __name__ == '__main__':
    main()
