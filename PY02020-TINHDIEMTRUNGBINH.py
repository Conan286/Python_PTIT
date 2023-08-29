import math

def main():
    n = int(input())
    a = sorted(list(map(float,input().split())))
    # print(a)
    l,r,n = 1,len(a)-2,len(a)
    while a[l] == a[0]:
        l += 1
    while a[r] == a[n-1]:
        r -= 1
    cnt = 0
    sum = 0.0
    while l<=r:
        sum += a[l]
        cnt += 1
        l += 1
    print('%.2f'%(sum/cnt))

if __name__ == "__main__":
    main()
