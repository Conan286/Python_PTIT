import math
from functools import cmp_to_key

def change(s,cnt):
    sum = 0
    for i in s:
        sum += ord(i)-48
    sum = str(sum)
    if len(sum) == 1: return cnt
    return change(sum,cnt+1)

def main():
    s = str(input())
    print(change(s,1))

if __name__ == '__main__':
    main()