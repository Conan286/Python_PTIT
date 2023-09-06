import math

def rev(s):
    ans = ""
    for i in s:
        ans = i+ans
    return ans
def mahoa2(s,k):
    ans = ""
    for i in s:
        if i=='.': v = 92 - 65
        elif i=='_': v = 91 - 65
        else:
            v = ord(i)-65
        v += k
        v %= 28
        if v<26: ans += chr(v+65)
        elif v==26: ans += "_"
        elif v==27: ans += "."
    return rev(ans)



def main():
    while 1:
        sc = input()
        if sc == "0": break
        k,s = sc.split()
        k = int(k)
        print(mahoa2(s,k))

if __name__ == '__main__':
    main()