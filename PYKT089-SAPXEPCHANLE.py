import math
from functools import cmp_to_key

def compare(item1, item2):
    return 1 if item1<item2 else (-1 if item1>item2 else 0)

def main():
    n = int(input())
    a = []
    while n:
        arr = list(map(int,input().split()))
        a += arr
        n -= len(arr)
    chan = sorted(list(filter(lambda x:x%2==0,a)))
    le   = sorted(list(filter(lambda x:x%2==1,a)),key=cmp_to_key(compare))
    index = []
    c,l = 0,0
    for i in range(len(a)):
        if a[i]%2==0:
            index.append(0)
        else:
            index.append(1)
    for i in index:
        if i==0:
            print(chan[c],end=' ')
            c+=1
        else:
            print(le[l],end=' ')
            l+=1

if __name__ == '__main__':
    main()
