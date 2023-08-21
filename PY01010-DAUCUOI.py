import math

def check(s):
    if (s[0] == s[-2]) and (s[1] == s[-1]):
        return 1
    return 0

def main():
    t = int(input())
    while t > 0:
        s = str(input())
        if (check(s) == 1):
            print("YES")
        else:
            print("NO")
        t -= 1

if __name__ == '__main__':
    main()
