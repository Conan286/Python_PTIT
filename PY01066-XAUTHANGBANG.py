def reverse(s):
    res=""
    for i in s:
        res = i + res
    return res
def check(s1, s2):
    n = len(s1)
    for i in range(n - 1):
        as1 = ord(s1[i])
        bs1 = ord(s1[i + 1])
        as2 = ord(s2[i])
        bs2 = ord(s2[i + 1])
        if abs(as1 - bs1) != abs(as2 - bs2):
            return 0
    return 1
def main():
        t = int(input())
        while(t>0):
            s1 = str(input())
            s2 = reverse(s1)
            n = len(s1)
            if(check(s1,s2)==1): print("YES")
            else : print("NO")
            t -= 1

if __name__=='__main__':
    main()