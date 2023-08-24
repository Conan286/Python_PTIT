import math

def main():
    t = int(input())
    while t:
         n = str(input())
         m = str(input())
         print(n.count(m))
         t -= 1

if __name__ == "__main__":
    main()