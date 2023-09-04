import math


def main():
    m,n = map(int,input().split())
    a = []
    vs = []
    dx = [1,1, 1,0, 0,-1,-1,-1 ]
    dy = [1,0,-1,1,-1,-1, 0, 1 ]
    for i in range(0,m):
        b = list(map(int,input().split()))
        c = [0 for i in range(0,n)]
        a.append(b)
        vs.append(c)
    ans = 0
    for i in range(0,m):
        for j in range(0,n):
            if a[i][j] == -1:
                for k in range(0,8):
                    vx = i+dx[k]
                    vy = j+dy[k]
                    if vx>=0 and vy>=0 and vx<m and vy<n and vs[vx][vy]==0:
                        ans += a[vx][vy]
                        vs[vx][vy] = 1

    print(ans)



if __name__ == '__main__':
    main()