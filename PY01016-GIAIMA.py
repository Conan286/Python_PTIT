import math

def giaima(s):
    st=""
    n = len(s)
    c = ''
    for i in s:
        if i.isalpha():
            c = i
        elif i.isdigit():
            k = ord(i) - 48
            for j in range (0,k):
                st+=c
    return st

def main():
        t = int(input())
        while t:
            s = str(input())
            print(giaima(s))
            t -= 1

if __name__ == "__main__":
    main()