def legendre(n,p):
    ans = 0
    i = p
    while(i<=n):
        ans += int(n/i)
        i *= p
    return ans
def main():
    t = int(input())
    while(t>0):
        n,p = map(int, input().split())
        print( legendre(n,p))
        t -= 1
if __name__ == '__main__':
    main()