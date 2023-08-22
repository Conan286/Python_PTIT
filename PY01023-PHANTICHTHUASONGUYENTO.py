import math
def pt(n):
        i = 1
        print(1,end=" ")
        for i in range (2,int(math.sqrt(n)+1)):
             cnt = 0
             if n%i ==0:
                while n%i==0:
                    n=int(n/i)
                    cnt += 1
                print("* ",end="")
                print(i,'^',cnt,sep="",end=" ")

        if n>1:
            print("* ",n,"^1",sep="",end="")
        print("")


def main():
    t = int(input())
    while(t>0):
        n = int(input())
        pt(n)
        t -= 1


if __name__ == '__main__':
    main()
