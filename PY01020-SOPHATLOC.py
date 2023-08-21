def check(s):
    n = len(s)
    if s[n-2]=='8' and s[n-1]=='6':
        return 1
    return 0

def main():
    t = int(input())
    while(t>0):
        s = str(input())
        if(check(s)): print("YES")
        else: print("NO")
        t -= 1
if __name__ == '__main__':
    main()