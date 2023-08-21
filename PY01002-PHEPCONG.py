s = str(input())
a = int(s[0])
b = int(s[4])
c = int(s[8])
if(s[2] == '+'):
    if (a+b == c):
        print("YES")
    else :
        print("NO")
if(s[2] == '-'):
    if (a-b == c):
        print("YES")
    else :
        print("NO")
if(s[2] == '*'):
    if (a*b == c):
        print("YES")
    else :
        print("NO")
if(s[2] == '/'):
    if (a/b == c):
        print("YES")
    else :
        print("NO")

