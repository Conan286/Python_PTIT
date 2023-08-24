import math

def soxenke(s):
   n = len(s)
   if n%2==0 or s[0]==s[1]:
       return 0
   i = 2
   while i<n :
       if s[i]!=s[i-2]:
           return 0
       i+=2
   return 1

def check(n):
    return "YES" if (soxenke(n)) else "NO"

def main():
    t = int(input())
    while t:
         n = str(input())
         print(check(n))
         t -= 1

if __name__ == "__main__":
    main()
