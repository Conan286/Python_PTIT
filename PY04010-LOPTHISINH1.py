import math
from functools import cmp_to_key


def main():
    name = str(input())
    birth = str(input())
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    print(name,birth,end=' ')
    print('%.1f'%(m1+m2+m3))

if __name__ == '__main__':
    main()