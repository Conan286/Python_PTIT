def check(s):
    n = len(s)
    for i in range(n-1):
        if s[i]>s[i+1]:
            return 0
    return 1
def main():
    t = int(input())
    while(t>0):
        s = str(input())
        if(check(s)) :
            print("YES")
        else:
            print("NO")
        t -= 1
if __name__ == '__main__':
    main()