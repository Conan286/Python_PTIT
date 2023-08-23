import math


def main():
    t = int(input())
    while t:
        x, y = map(int, input().split())
        inp = list(input().split())
        if (len(inp) > 1):
            s1, s2 = inp[0], inp[1]
        else:
            s1, s2 = inp[0], input()
        p = str(min(x, y))
        q = str(max(x, y))
        n1 = int(s1.replace(q, p)) + int(s2.replace(q, p))
        n2 = int(s1.replace(p, q)) + int(s2.replace(p, q))
        print(n1, n2)
        t -= 1


if __name__ == "__main__":
    main()
