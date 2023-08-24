import math

def sum(n):
    s = 0.0
    i = 1
    if n%2 == 0: i = 2
    while i<=n:
        s += 1.0/i
        i += 2
    return s

def main():
    t = int(input())
    while t:
         n = int(input())
         print('%.6f'%sum(n))
         t -= 1

if __name__ == "__main__":
    main()
