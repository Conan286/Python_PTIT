import math

def prime(n):
    k = int(math.sqrt(n))
    for i in range (2,k+1):
        if n%i == 0:
            return 0
    return 1 if n>1 else 0

def chusonguyento(s):
   i = 0
   n = len(s)
   if prime(n)==0 : return 0
   c1, c2 = 0, 0
   for i in s:
       if i=='2' or i=='3' or i=='5' or i=='7':
           c1 +=1
       else:
           c2 +=1
   return 1 if c1>c2 else 0

def check(n):
    return "YES" if (chusonguyento(n)) else "NO"

def main():
    t = int(input())
    while t:
         n = str(input())
         print(check(n))
         t -= 1

if __name__ == "__main__":
    main()
