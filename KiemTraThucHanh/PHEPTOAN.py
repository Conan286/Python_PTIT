n,m = map(int,input().split())
a = list(map(int,input().split()))
d,possible = n-1,0
phepToan,ToanTu = [""]*d,["+","-","*"]

def check():
    #bien toan cuc
    global possible
    s = str(a[0])
    if a[0]<0: s = "("+str(a[0])+")"
    for i in range(d):
        s += phepToan[i]
        if a[i+1] < 0: s += "("+str(a[i+1])+")"
        else : s+= str(a[i+1])
    if eval(s) == m:
        s += "=" + str(m)
        print(s)
        possible = 1
def Try(i):
    for j in ToanTu:
        phepToan[i] = j
        if i == d - 1: check()
        else: Try(i+1)
def main():
    Try(0)
    if possible==0:
        print("IMPOSSIBLE")
if __name__ == '__main__':
    main()

