import math

def cunghoangdao(d,m):
    if (d>=21 and m==3) or (d<=19 and m==4):
        return "Bach Duong"
    elif (d>=20 and m==4) or (d<=20 and m==5):
        return "Kim Nguu"
    elif (d>=21 and m==5) or (d<=20 and m==6):
        return "Song Tu"
    elif (d>=21 and m==6) or (d<=22 and m==7):
        return "Cu Giai"
    elif (d>=23 and m==7) or (d<=22 and m==8):
        return "Su Tu"
    elif (d>=23 and m==8) or (d<=22 and m==9):
        return "Xu Nu"
    elif (d>=23 and m==9) or (d<=22 and m==10):
        return "Thien Binh"
    elif (d>=23 and m==10) or (d<=22 and m==11):
        return "Thien Yet"
    elif (d>=23 and m==11) or (d<=21 and m==12):
        return "Nhan Ma"
    elif (d>=22 and m==12) or (d<=19 and m==1):
        return "Ma Ket"
    elif (d>=20 and m==1) or (d<=18 and m==2):
        return "Bao Binh"
    elif (d>=19 and m==2) or (d<=20 and m==3):
        return "Song Ngu"

def main():
        t = int(input())
        while t:
            d,m = map(int,input().split())
            print(cunghoangdao(d,m))
            t -= 1

if __name__ == "__main__":
    main()