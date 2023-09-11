import math
import re
from functools import cmp_to_key
import sys

def main():
      t = int(input())
      while t:
          s = str(input())
          s1 = str(input())
          print(s.count(s1))
          t -= 1
if __name__ == '__main__':
    main()