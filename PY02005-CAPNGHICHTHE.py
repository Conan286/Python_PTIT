import math


def scnt(a):
    n = len(a)
    cnt = 0
    for i in range(0,n):
        for j in range (i+1,n):
            if a[i] > a[j] :
                cnt += 1
    return cnt



def main():
    n = int(input())
    a =  list(map(int, input().split()))
    print(scnt(a))


if __name__ == "__main__":
    main()
