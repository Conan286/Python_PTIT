import math
def maxs(s):
    ans = 0
    n = len(s)
    i = 0
    while i<n:
        if(s[i]>='0' and s[i]<='9'):
            sum = 0
            while(i<n and s[i]>='0' and s[i]<='9'):
                sum = sum*10 + ord(s[i])-48
                i += 1
            ans = max(ans,sum)
        else: i+=1
    return ans

def main():
       t = int(input())
       while t>0:
           s = str(input())
           print(maxs(s))
           t -= 1

if __name__ == '__main__':
    main()
