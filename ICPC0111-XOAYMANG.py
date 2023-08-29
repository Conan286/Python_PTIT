import math

def main():
        t = int(input())
        while t:
            n,k = map(int,input().split())
            a = list(map(int,input().split()))
            b = []
            for i in a[(k-n):]:
                b.append(i)
            for i in a[:(k%n)]:
                b.append(i)
            for j in b:
                print(j,end = ' ')
            print()
            t -= 1

if __name__ == "__main__":
    main()