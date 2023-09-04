import math
def main():
    t = int(input())
    newset = set()
    while t:
        s = str(input())
        newset.add(s)
        t -= 1
    print(len(newset))
if __name__ == '__main__':
    main()