import math


def main():
       m,n = map(int,input().split())
       a = []
       for i in range (0,m):
           b = list(map(int,input().split()))
           a.append(b)
       ar = []
       if m>n:
            h = m-n
            h = 2*h - 2
            for i in range(1,h,2):
                ar.append(a[i])
            for i in range(h+1,m):
                ar.append(a[i])
       else:
           c = n-m
           c = c*2 - 1
           for i in range (0,m):
               br = []
               for j in range(0,c,2):
                   br.append(a[i][j])
               for j in range(c+1,n):
                   br.append(a[i][j])
               ar.append(br)
       l = min(m,n)
       for i in range(0,l):
           for j in range (0,l):
               print(ar[i][j],end=" ")
           print()

if __name__ == '__main__':
    main()