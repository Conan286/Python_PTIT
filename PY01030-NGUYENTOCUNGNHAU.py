import math

def gcd(a,b):
    return b if (a%b==0) else gcd(b,a%b)

def nguyentocungnhau(n,k):
    i = 1
    a = int(math.pow(10,k-1))
    b = int(math.pow(10,k))
    while a<b:
        if gcd(n,a)==1:
            print(a,end=' ')
            if i%10 == 0:
                print()
            i += 1
        a += 1

def main():
        n,k = map(int,input().split())
        nguyentocungnhau(n,k)

if __name__ == "__main__":
    main()