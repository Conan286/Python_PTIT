import math

def main():
       m,n = map(int,input().split())
       a = []
       ans = 0
       check = 0
       maxNum = 0
       minNum = 10000
       for i in range (0,m):
           b = list(map(int,input().split()))
           maxNum = max(max(b),maxNum)
           minNum = min(min(b),minNum)
           a.append(b)
       soMayMan = maxNum - minNum
       for i in a:
           for j in i:
               if j == soMayMan:
                   check = 1
                   break
       if check:
           print(soMayMan)
           for i in range(0, m):
               for j in range(0, n):
                   if a[i][j] == soMayMan:
                       print("Vi tri [", i, "][", j, "]", sep="")
                       check = 1

       else:
           print("NOT FOUND")

if __name__ == '__main__':
    main()