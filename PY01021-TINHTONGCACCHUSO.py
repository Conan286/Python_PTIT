import math

def main():
    t = int(input())
    while t:
        a = str(input())
        sum = 0
        ans =""
        for i in a:
            if i.isdigit():
                sum += ord(i) -48
            else:
                ans += i
        b = sorted(list(ans))
        print("".join(b),sum,sep='')
        t -= 1

if __name__ == "__main__":
    main()
