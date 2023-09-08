import math

N = 10**4
p = [1]*N
prime = []
def sang():
    k = int(math.sqrt(N))+1
    p[0] = p[1] = 0
    for i in range(2,k):
        if p[i]:
            for j in range(i*i,N,i):
                p[j] = 0
    for i in range(N):
        if p[i]: prime.append(i)


def main():
    sang()
    n,x = map(int,input().split())
    for i in range(n+1):
        print(x,end=' ')
        x += prime[i]

if __name__ == '__main__':
    main()