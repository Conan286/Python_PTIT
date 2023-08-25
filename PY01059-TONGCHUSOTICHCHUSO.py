import math

def tongchuso_tichchuso(s):
    sum = 0
    mul = 1
    cm = 0
    n = len(s)
    i = 0
    while i<n:
        sum += int(s[i])
        i += 2
    i = 1
    while i < n:
        k = int(s[i])
        if k:
          mul *= k
          cm = 1
        i += 2
    if cm==0:
        mul = 0
    print(sum,mul)

def main():
        t = int(input())
        while t:
            s = str(input())
            tongchuso_tichchuso(s)
            t -= 1

if __name__ == "__main__":
    main()