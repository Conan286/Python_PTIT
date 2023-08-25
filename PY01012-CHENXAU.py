import math

def gcd(a,b):
    return b if (a%b==0) else gcd(b,a%b)

def bobanguyentocungnhau(l,r):
    for i1 in range (l,r-1,1):
        for i2 in range(i1+1, r , 1):
            for i3 in range(i2 + 1, r+1, 1):
                if gcd(i1,i2)==1 and gcd(i2,i3)==1 and gcd(i3,i1)==1:
                    print("(",i1,", ",i2,", ",i3,")",sep='')


def main():
        s1 = str(input())
        s2 = str(input())
        p = int(input())
        p -= 1
        print(s1[:p]+s2+s1[p:])

if __name__ == "__main__":
    main()