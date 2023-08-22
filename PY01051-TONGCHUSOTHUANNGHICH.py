import math
def rev(s):
    s1=""
    for i in s:
        s1 = i+s1
    return s1
def sum(s):
    ans = 0
    for i in s:
        ans+=ord(i)-48
    return str(ans)
def check(s):
    return "YES" if (rev(sum(s))==sum(s) and len(sum(s))>1) else "NO"

def main():
        t = int(input())
        while t>0:
            s = str(input())
            print(check(s))
            t -=1

if __name__ == '__main__':
    main()
