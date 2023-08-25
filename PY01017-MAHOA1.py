import math

def mahoa1(s):
    st=""
    n = len(s)
    c = s[0]
    i = 0
    cnt = 1
    while i<n:
        if i<n-1 and s[i]==s[i+1]: cnt += 1
        elif i<n-1 and s[i]!=s[i+1]:
            st += str(cnt)+c
            c = s[i+1]
            cnt = 1
        elif i==n-1:
            st += str(cnt) + c
        i+=1
    return st

def main():
        t = int(input())
        while t:
            s = str(input())
            print(mahoa1(s))
            t -= 1

if __name__ == "__main__":
    main()