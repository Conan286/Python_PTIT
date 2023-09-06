import math

def soDep(s):
    newSet = set()
    for i in s:
        newSet.add(i)
    if len(newSet)!=2: return 0
    k = abs(ord(s[1])-ord(s[0]))
    for i in range(2,len(s)):
        h = abs(ord(s[i])-ord(s[i-1]))
        if h!=k:
            return 0
    return 1

def check(s):
    return "YES" if soDep(s) else "NO"

def main():
    t = int(input())
    while t:
        s = str(input())
        print(check(s))
        t -= 1
if __name__ == '__main__':
    main()