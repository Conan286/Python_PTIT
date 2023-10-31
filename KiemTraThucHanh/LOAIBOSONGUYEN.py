import math
import os
import re


def main():
    file = open('DATA.in','r')
    mp = [file.read().split('\n')]
    mps = []
    for w in mp[0]:
        for s in w.split():
            try:
                k = int(s)
                if(k>2147483647 or k<-2147483647):
                    mps.append(s)
            except:
                mps.append(s)
    mps.sort()
    for i in mps: print(i,end=" ")


if __name__ == '__main__':
    main()
