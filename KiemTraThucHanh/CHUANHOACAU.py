from math import *
from functools import cmp_to_key
import re
import io
import os
import sys
import time
import array as arr


def main():
    # file = open('data.in','r')
    a = []
    while 1:
        try:
            b = list(map(str,input().lower().split('\n')))
            for it in b:
                it=it.replace(".",".;")
                it=it.replace("?","?;")
                it=it.replace("!","!;")
                l = list(map(str,it.split(';')))
                for i in l:
                    s = ""
                    w = list(i.split())
                    n = len(w)
                    if(n>1):
                        for j in range(n-1):
                            if j==0: s+= w[0].title()+" "
                            else: s+=w[j]+" "
                        if w[n-1]!="?" and w[n-1]!="!" and w[n-1]!=".": s+=w[n-1]
                        else:
                            while s[-1]==" ": s = s[:-1]
                            s+=w[n-1]
                        if s[len(s)-1]!="." and s[len(s)-1]!="!" and s[len(s)-1]!="?":
                            s+="."
                        a.append(s)
        except Exception:
            break
    for i in a:
       print(i)


if __name__ == '__main__':
    main()