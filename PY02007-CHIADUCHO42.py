import math
def main():
    cnt = 10
    set42 = set()
    while cnt:
        s = list(map(int,input().split()))
        n = len(s)
        for item in s:
            set42.add(item%42)
        cnt -= n
    print(len(set42))



if __name__ == '__main__':
    main()