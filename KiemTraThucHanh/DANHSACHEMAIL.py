import math
from functools import cmp_to_key
import re
def main():
    file = open('CONTACT.in','r')
    l = list(file.read().lower().split('\n'))
    s = set(l)
    s = sorted(list(s))
    for e in s:
        print(e)

if __name__ == '__main__':
    main()