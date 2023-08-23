import math

def sotanggiam(s):
   i = 0
   n = len(s)
   if(n<3): return 0
   while(i<n-1 and s[i]<s[i+1]): i+=1
   while(i<n-1 and s[i]>s[i+1]): i+=1
   return 1 if i==n-1 else 0

def check(n):
    return "YES" if (sotanggiam(n)) else "NO"

def main():
    t = int(input())
    while t:
         n = str(input())
         print(check(n))
         t -= 1

if __name__ == "__main__":
    main()
