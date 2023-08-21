import math
def main():
  a,k,n = map(int,input().split())
  h = n - a
  if(a%k==0):
      b=k
  else:
      z = int(a/k)
      b = k*(z+1)-a
  check = 0
  while b<=h:
      print(b,end=' ')
      b+=k
      check = 1
  if check == 0:
      print("-1")

if __name__ == '__main__':
    main()
