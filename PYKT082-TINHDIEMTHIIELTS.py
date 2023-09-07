import math
from functools import cmp_to_key

def score(n):
    if   n >= 39: return 9.0
    elif n >= 37: return 8.5
    elif n >= 35: return 8.0
    elif n >= 33: return 7.5
    elif n >= 30: return 7.0
    elif n >= 27: return 6.5
    elif n >= 23: return 6.0
    elif n >= 20: return 5.5
    elif n >= 16: return 5.0
    elif n >= 13: return 4.5
    elif n >= 10: return 4.0
    elif n >=  7: return 3.5
    elif n >=  5: return 3.0
    elif n >=  3: return 2.5
    return 1.0

def roundScore(p):
    r = int(p)
    i = p - r
    p = float(r)
    if   i>=0.75: p += 1
    elif i>=0.25: p += 0.5
    if p>9: p = 9
    return p

def main():
    t = int(input())
    while t:
       r,l,s,w = map(float,input().split())
       reading   = int(r)
       listening = int(l)
       r = score(reading)
       l = score(listening)
       overall = (r+l+s+w)/4.0
       print(roundScore(overall))
       t -= 1

if __name__ == '__main__':
    main()