from sys import stdin, stdout, setrecursionlimit

n = int(stdin.readline())
adj_list = [[] for _ in range(2 * n + 1)]
visited = [0] * (2 * n + 1)
name_mapping, value = dict(), 1

setrecursionlimit(pow(10, 5) + 1)

def DFS(u):
    visited[u] = 1
    for v in adj_list[u]:
        if not visited[v]:
            if DFS(v):
                return True
        elif visited[v] == 1:
            return True
    visited[u] = 2
    return False

def solve():
    for i in range(1, value):
        if not visited[i]:
            if DFS(i):
                return "impossible"
    return "possible"
if __name__ == '__main__':
    for _ in range(n):
        comparison = stdin.readline().split()
        if comparison[0] not in name_mapping:
            name_mapping[comparison[0]] = value
            value += 1
        if comparison[2] not in name_mapping:
            name_mapping[comparison[2]] = value
            value += 1
        if comparison[1] == '>':
            adj_list[name_mapping[comparison[0]]].append(name_mapping[comparison[2]])
        else:
            adj_list[name_mapping[comparison[2]]].append(name_mapping[comparison[0]])
    print(solve())