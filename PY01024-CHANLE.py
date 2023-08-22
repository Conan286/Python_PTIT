import math

def check(s):
    sum = int(0)
    for i in s:
        sum+=ord(i)-48
    n = len(s)
    for i in range(0,n-1):
        a = abs(ord(s[i])-ord(s[i+1]))
        if(a!=2):
            return "NO"
    return "YES" if (sum%10==0) else "NO"

def main():
    t = int(input())
    while(t>0):
        s = str(input())
        print(check(s))
        t -= 1

if __name__ == '__main__':
    main()
