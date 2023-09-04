import math

def biendoi(n):
    if n==1 :
        return 1
    newset = set()
    newset.add(n)
    while n!=1:
        if n%2 == 0:
            n //= 2
            newset.add(n)
        else:
            n = n*3 + 1
            newset.add(n)
    return len(newset)

def main():
    i = 1
    while "Manchester is red":
        n = int(input())
        if(n==0):
            break
        print(biendoi(n))

if __name__ == '__main__':
    main()