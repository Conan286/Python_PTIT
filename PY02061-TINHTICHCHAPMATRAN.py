import math


def main():
    t = int(input())
    while t:
        m,n = map(int,input().split())
        x = []
        for i in range(0,m):
            b = list(map(int,input().split()))
            x.append(b)
        k = []
        for j in range(0,3):
            kernel = list(map(int,input().split()))
            k.append(kernel)
        sum = 0
        for row in range(0,m-2):
            for col in range(0,n-2):
                s = 0
                for h in range (0,3):
                    for c in range (0,3):
                        s += k[h][c]*x[row+h][col+c]
                sum += s
        print(sum)
        t -= 1

if __name__ == '__main__':
    main()