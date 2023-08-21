import math
def hanoi(n,a,b,c):
    if n==1 :
        print(a,c,sep=" -> ")
        return
    hanoi(n-1,a,c,b)
    hanoi(1,a,b,c)
    hanoi(n-1,b,a,c)

def main():
    n = int(input())
    hanoi(n,'A','B','C')

if __name__ == '__main__':
    main()
