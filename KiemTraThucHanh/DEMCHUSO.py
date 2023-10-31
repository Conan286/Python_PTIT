def xuly(x, A):
    if A == 0:
        return 0
    B = A
    t = 0
    mu10 = 1
    while B >= 10:
        B = B // 10
        t += 1
        mu10 = mu10 * 10
    y = A // mu10
    a = A - y * mu10
    if y < x:
        return y * t * (mu10 // 10) + xuly(x, a)
    elif y > x:
        return mu10 + y * t * (mu10 // 10) + xuly(x, a)
    elif y == x:
        return a + 1 + y * t * (mu10 // 10) + xuly(x, a)

def sochuso(A):
    KQ = 0
    B = A
    t = 0
    mu10 = 1
    while B >= 10:
        B = B // 10
        t += 1
        mu10 = mu10 * 10
    for i in range(1, t + 1):
        nhan10 = 9 * i
        for j in range(2, i + 1):
            nhan10 = nhan10 * 10
        KQ = KQ + nhan10
    KQ = KQ + (A - mu10 + 1) * (t + 1)
    return KQ
def main():
    t = int(input())
    while t:
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        hieu = 0
        u = [0] * 10
        for i in range(1, 10):
            u[i] = xuly(i, b) - xuly(i, a - 1)
            hieu = hieu + u[i]
        u[0] = sochuso(b) - sochuso(a - 1) - hieu
        for i in range(10):
            print(u[i], end=' ')
        print()
        t -= 1
if __name__ == '__main__':
    main()