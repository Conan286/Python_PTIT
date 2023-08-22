import math
def sum(s):
    ans = 0
    for i in s:
        ans+=ord(i)-48
    return 1 if ans%3==0 else 0

def check(s):
    return "YES" if sum(s) else "NO"

def main():
        t = int(input())
        while t>0:
            s = str(input())
            print(check(s))
            t -=1

if __name__ == '__main__':
    main()
