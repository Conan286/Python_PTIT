import math

def main():
       t = int(input())
       while t:
           n = int(input())
           a = list(map(int,input().split()))
           freg = {}
           ans = -1
           for i in a:
               if i in freg:
                   freg[i] += 1
               else:
                   freg[i] = 1
           for key,val in freg.items():
               if val%2!=0:
                   ans = key
           print(ans)
           t -= 1



if __name__ == '__main__':
    main()