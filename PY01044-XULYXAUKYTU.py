import math
from functools import cmp_to_key

def main():
    set1 = set(map(str, input().lower().split()))
    set2 = set(map(str, input().lower().split()))
    set3 = sorted(set1.union(set2))
    set4 = sorted(set1.intersection(set2))
    for i in set3: print(i,end=' ')
    print()
    for i in set4: print(i, end=' ')

if __name__ == '__main__':
    main()