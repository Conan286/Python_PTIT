import math

def isPrime(n):
    if n<2:
        return 0
    k = int(math.sqrt(n))
    for i in range (2,k+1):
        if n%i == 0:
            return 0
    return 1

def main():
       m,n = map(int,input().split())
       a = []
       ans = 0
       check = 0
       for i in range (0,m):
           b = list(map(int,input().split()))
           for j in b:
               if isPrime(j):
                   check = 1
                   ans = max(ans,j)
           a.append(b)
       if check==0:
           print("NOT FOUND")
       else:
           print(ans)
           for i in range (0,m):
               for j in range (0,n):
                   if a[i][j] == ans:
                       print("Vi tri [",i,"][",j,"]",sep="")

if __name__ == '__main__':
    main()