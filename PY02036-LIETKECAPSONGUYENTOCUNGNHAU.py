import math

def ntcn(a):
    n = len(a)
    for i in range(0,n):
        for j in range (i+1,n):
            if(math.gcd(a[i],a[j])==1):
                print(a[i],a[j])

def main():
    n = int(input())
    a =  sorted(list(map(int, input().split())))
    ntcn(a)

if __name__ == "__main__":
    main()
