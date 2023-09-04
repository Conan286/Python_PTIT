import math

def isPrime(n):
    if n<2: return 0
    k = int(math.sqrt(n))
    for i in range(2,k+1):
        if n%i==0:
            return 0
    return 1

def main():
        n = int(input())
        j = n/2
        freg = {}
        a = list(map(int,input().split()))
        for item in a:
            if(isPrime(item)):
                if item in freg:
                    freg[item] += 1
                else:
                    freg[item] = 1
        for k,v in freg.items():
            print(k,v)

if __name__ == '__main__':
    main()