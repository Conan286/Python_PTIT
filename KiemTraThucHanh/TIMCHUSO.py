#   x(n) = (3+sqrt(5))^n
#   a(n) = (3+sqrt(5))^n + (3-sqrt(5))^n => x(n) = a(n) - (3-sqrt(5))^n
#   phuong trinh dac trung (r-(3+sqrt(5)))*(r-(3+sqrt(5))) = 0 => r^2-6r+4=0
# =>He thuc truy hoi la a(n) = 6a(n-1)-4a(n-2) voi a0 = 2 va a1 = 6
# Ta thay 0<(3-sqrt(5))^n <=1 => 3 chu so cuoi cua (3+sqrt(5))^n la 3 chu so cuoi cua a(n) tru 1
# Quy luat la cu 200 so se lap lai 3 chu so cuoi
#Ngoai le voi n>200 khi n%200<3
import math
import re


a = [0]*203


def main():
   a[0] = 2
   a[1] = 6
   for i in range(2,203):
       a[i] = 6*a[i-1]-4*a[i-2]
   a1 = []
   a2 = []
   for i in range(200):
       S = str(a[i]-1)[-3:]
       while len(S)<3: S="0"+S
       a1.append(S)
   for i in range(200,203):
       S = str(a[i] - 1)[-3:]
       while len(S) < 3: S = "0" + S
       a2.append(S)
   t = int(input())
   for i in range(1,t+1):
       n = int(input())
       if n>=200 and n%200<3:
           print("Case #"+str(i)+": "+a2[n%200])
       else:
           print("Case #" +str(i)+ ": " + a1[n % 200])



if __name__ =='__main__':
    main()