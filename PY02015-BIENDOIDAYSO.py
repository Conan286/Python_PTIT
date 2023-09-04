import math

def biendoi(a,b,c,d):
    cnt = 0
    while "Manchester United":
        if (a==b and b==c and c==d):
            break
        a,b,c,d = abs(a-b),abs(b-c),abs(c-d),abs(d-a)
        cnt += 1
    return cnt

def main():
    while "Manchester is red":
        a,b,c,d = map(int,input().split())
        if a==0 and b==0 and c==0 and d==0:
            break;
        print(biendoi(a,b,c,d))

if __name__ == '__main__':
    main()