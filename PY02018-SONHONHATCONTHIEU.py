import math


def sct(a):
    n = len(a)
    i = 1
    if a[0]>1:
        return 1
    else:
        #bai nay co ca truong hop a[0]<1 moi vl chu =))
        while i<n:
            if a[i]-a[i-1]>1:
                return a[i-1]+1
            else: i+=1
    return a[n-1]+1



def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(sct(a))


if __name__ == "__main__":
    main()
