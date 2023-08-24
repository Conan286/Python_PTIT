import math

def prime(n):
    k = int(math.sqrt(n))
    for i in range (2,k+1):
        if n%i == 0:
            return 0
    return 1 if n>1 else 0

def chanlenguyento(s):
   i = 0
   n = len(s)
   sum = 0
   while i<n:
       k = ord(s[i])-48
       if (i%2 == 0 and k%2!=0 ) or (i%2 != 0 and k%2==0):
           return 0
       sum += k
       i += 1
   return 1 if prime(sum) else 0

def check(n):
    return "YES" if (chanlenguyento(n)) else "NO"

def main():
    t = int(input())
    while t:
         n = str(input())
         print(check(n))
         t -= 1

if __name__ == "__main__":
    main()