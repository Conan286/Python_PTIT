import math


def main():
       t = int(input())
       while t:
           n = int(input())
           a = set(map(int,input().split()))
           print(max(a)-min(a)-len(a)+1)
           t -= 1

if __name__ == '__main__':
    main()