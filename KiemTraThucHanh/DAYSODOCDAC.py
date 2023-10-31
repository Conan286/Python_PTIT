import math

def main():
    t = int(input())
    while t:
        n = int(input())
        mp = {}
        a = list(map(int,input().split()))
        check = "YES"


        for i in a:
            if i in mp:
                mp[i] += 1
                if mp[i]>1: check = "NO"

            else:
                mp.clear()
                mp[i] = 1




        print(check)
        t -= 1

if __name__ == '__main__':
    main()