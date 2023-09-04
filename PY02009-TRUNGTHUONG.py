import math

def main():
    t = int(input())
    while t:
        n = int(input())
        freg = {}
        while n:
            x = int(input())
            if x in freg:
                freg[x] += 1
            else:
                freg[x] = 1
            n -= 1
        value = 0
        for k,v in freg.items():
            value = max(v,value)
        key = 1000
        for k,v in freg.items():
            if v == value:
                key = min(key,k)
        print(key)
        t -= 1

if __name__ == '__main__':
    main()