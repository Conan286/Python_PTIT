import math


def main():
    m,n = map(int,input().split())
    uc = math.gcd(m,n)
    m //= uc
    n //= uc
    print(m,"/",n,sep='')

if __name__ == '__main__':
    main()