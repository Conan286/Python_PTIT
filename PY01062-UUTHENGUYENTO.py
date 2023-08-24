import math

def prime(n):
    k = int(math.sqrt(n))
    for i in range (2,k+1):
        if n%i == 0:
            return 0
    return 1 if n>1 else 0

def uuthenguyento(s):
   i = 0
   n = len(s)
   if prime(n)==0: return 0
   c1,c2=0,0
   while i<n:
       k = ord(s[i])-48
       if prime(k): c1+=1
       else: c2+=1
       i += 1
   return 1 if c1>c2 else 0

def check(n):
    return "YES" if (uuthenguyento(n)) else "NO"

def main():
    t = int(input())
    while t:
         n = str(input())
         print(check(n))
         t -= 1

if __name__ == "__main__":
    main()