import math
def toBase(N, b):
    ans = ""
    while N:
        k = N%b
        if k<10: ans=str(k)+ans
        else: ans=chr(k+55)+ans
        N //= b
    return ans

def main():
    t = int(input())
    while t:
        k = int(input())
        s = str(input())
        s = int(s,2)
        print(toBase(s,k))
        t -= 1

if __name__ == "__main__":
    main()