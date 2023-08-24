import math

def prime(n):
    k = int(math.sqrt(n))
    for i in range (2,k+1):
        if n%i == 0:
            return 0
    return 1 if n>1 else 0

def vitringuyento(s):
   i = 0
   n = len(s)
   while i<n:
       k = ord(s[i])-48
       if (prime(i) == 0 and prime(k)!=0 ) or (prime(i) != 0 and prime(k)==0):
           return 0
       i += 1
   return 1

def check(n):
    return "YES" if (vitringuyento(n)) else "NO"

def main():
    t = int(input())
    while t:
         n = str(input())
         print(check(n))
         t -= 1

if __name__ == "__main__":
    main()