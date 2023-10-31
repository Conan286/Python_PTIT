from collections import deque
n = int(input())
dq = deque()
dq.append([int(input()), 1])
cnt = 0
for i in range(1, n):
    x = int(input())
    while len(dq) > 0:
        if x < dq[-1][0]:
            cnt += 1
            dq.append([x, 1])
            break
        else:
            tmp = dq.pop()
            cnt += tmp[1]
            if tmp[0] == x:
                cnt += 1 if len(dq) > 0 else 0
                dq.append([x, tmp[1] + 1])
                break
    if len(dq) == 0:
        dq.append([x, 1])
print(cnt)