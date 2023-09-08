import math
from functools import cmp_to_key

def check(s,sc):
    if len(s)!=len(sc): return 0
    n = len(sc)
    for i in range (n):
        if sc[i] == '?':
            continue
        elif s[i] != sc[i]:
            return 0
    return 1

def phepToanCoBan(s):
    if s[3] == "/" or s[3]=="*":
        return "WRONG PROBLEM!"
    for i in range(10,100):
        for j in range(10,100):
            x1 = ""
            k = i+j
            if k>99: break
            x1 = str(i)+" + "+str(j)+" = "+str(k)
            if check(x1, s) and (k>=10 and k<=99): return x1
    for i in range(20, 100):
        for j in range(10, i-9,1):
            x1 = ""
            k = i - j
            x1 = str(i) + " - " + str(j) + " = " + str(k)
            if check(x1, s) and (k >= 10 and k <= 99): return x1
    return "WRONG PROBLEM!"

def main():
   t = int(input())
   while t:
       s = str(input())
       print(phepToanCoBan(s))
       t -= 1

if __name__ == '__main__':
    main()