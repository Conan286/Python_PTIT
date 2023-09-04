import math
def main():
    s = str(input())
    if(len(s)==1):
        print(s)
    else:
        while len(s)>1:
            n = len(s)
            k = int(n/2)
            s1 = int(s[:k])
            s2 = int(s[k:])
            s = str(s1+s2)
            print(s)

if __name__ == '__main__':
    main()