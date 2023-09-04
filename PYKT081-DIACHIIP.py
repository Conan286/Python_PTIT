import math

def check(ip):
    if len(ip) != 4:
        return "NO"
    for i in ip:
        for kitu in i:
            if kitu < '0' or kitu > '9':
                return "NO"
    for i in ip:
        if int(i) > 255 or int(i) < 0:
            return "NO"
    return "YES"


def main():
    t = int(input())
    while t:
        ip = list(map(str, input().split('.')))
        print(check(ip))
        t -= 1


if __name__ == '__main__':
    main()
