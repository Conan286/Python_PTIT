import math

def soThuanNghich(n):
    s1 = str(n)
    s2 = rev(s1)
    return 1 if (s1==s2 and len(s1)>1) else 0
def rev(s):
    a = ""
    for i in s:
        a = i+a
    return a

def main():
       m,n = map(int,input().split())
       a = []
       ans = 0
       check = 0
       for i in range (0,m):
           b = list(map(int,input().split()))
           for j in b:
               if soThuanNghich(j):
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