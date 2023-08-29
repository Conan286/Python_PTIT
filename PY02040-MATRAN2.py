import math

def main():
    n = int(input())
    a = []
    for i in range(0,n):
        b = list(map(int,input().split()))
        a.append(b)
    k = int(input())
    lt,ld = 0,0
    for i in range(0,n):
        for j in range(n-i,n):
            ld += a[i][j]
    for i in range(0,n):
        for j in range(0,n-i-1):
            lt += a[i][j]
    dcd = int(math.fabs(lt-ld))
    if(dcd>k):
        print("NO")
    else:
        print("YES")
    print(dcd)

if __name__ == "__main__":
    main()
