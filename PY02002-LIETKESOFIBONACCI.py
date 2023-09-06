import math

fibo = []
def generation():
    fibo.append(0)
    fibo.append(1)
    for i in range (2,94):
        fibo.append(fibo[i-1]+fibo[i-2])

def fibonacci(a,b):
    for i in range(a,b+1):
        print(fibo[i],end=' ')
    print()
def main():
    generation()
    t = int(input())
    while t:
        a,b = map(int,input().split())
        fibonacci(a,b)
        t-=1
if __name__ == '__main__':
    main()