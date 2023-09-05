import math

def main():
       n = int(input())
       a = []
       freg = {}
       check = 0
       while n:
           b = list(map(int,input().split()))
           for j in b:
               a.append(j)
           n -= len(b)
       maxNum = max(a)
       for i in range(1,maxNum):
           if i in a:
               continue
           else:
               print(i)
               check = 1
       if check==0:
           print("Excellent!")


if __name__ == '__main__':
    main()