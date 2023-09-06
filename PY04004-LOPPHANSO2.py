import math


def main():
    a,b,c,d = map(int,input().split())
    t = a*d + b*c
    m = b*d
    uc = math.gcd(t,m)
    t//=uc
    m//=uc
    print(t,"/",m,sep='')

if __name__ == '__main__':
    main()