import math


def prime(n):
    if n<2: return 0
    k = int(math.sqrt(n))+1
    for i in range(2,k):
        if n%i==0:
            return 0
    return 1

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(0,n):
        b = list(map(int,input().split()))
        for j in range(0,m):
            if prime(b[j]): b[j] = 1
            else: b[j] = 0
        a.append(b)
    for r in a:
        for c in r:
            print(c,end= ' ')
        print()

if __name__ == "__main__":
    main()
