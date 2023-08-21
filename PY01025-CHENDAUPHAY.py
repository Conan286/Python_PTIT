import math
def rev(s):
    ans =''
    for i in s:
        ans = i+ans
    return ans

def main():
    s = str(input())
    s2 = ''
    n = len(s)
    i = n-1
    while(i>=0):
        s2 += s[i]
        if i>0 and (n-i)%3==0:
            s2+=','
        i -= 1
    print(rev(s2))



if __name__ == '__main__':
    main()
