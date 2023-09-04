import math

def main():
    t = int(input())
    while t:
        n = int(input())
        j = n/2
        freg = {}
        a = list(map(int,input().split()))
        for item in a:
            if item in freg:
                freg[item] += 1
            else:
                freg[item] = 1
        ans = "NO"
        for k,v in freg.items():
            if v>j:
                ans = k
                break
        print(ans)
        t -= 1

if __name__ == '__main__':
    main()