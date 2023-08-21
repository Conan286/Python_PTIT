def check(s):
    for i in s:
        if (i!='1' and i!='2' and i!='0'):
            return 0
    return 1
    
def main():
    t = int(input())
    while(t>0):
        s = str(input())
        if(check(s)): print("YES")
        else: print("NO")
        t -= 1
if __name__ == '__main__':
    main()