import math
def main():
    m,n = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    sa = set(a)
    sb = set(b)
    if sa==sb: print("YES")
    else : print("NO")
if __name__ == '__main__':
    main()