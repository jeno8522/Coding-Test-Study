import sys
from collections import Counter

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def UDLR(com):
    if com == 'U':
        return 0
    elif com == 'D':
        return 1
    elif com == 'L':
        return 2
    else:
        return 3

def dfs(r, c, v):
    global ans
    i = UDLR(graph[r][c])
    nr = r + dr[i]
    nc = c + dc[i]
    visited[r][c] = True
    u = nr * m + nc
    if visited[nr][nc]:
        if parent[u] == v:
            ans += 1
        return
    visited[nr][nc] = True

    union(v, u)
    dfs(nr, nc, v)

def findSet(v):
    if parent[v] == v:
        return v
    parent[v] = findSet(parent[v])
    return parent[v]
def union(v, u):
    parent[findSet(u)] = findSet(v)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    parent = [0] * (n * m)

    for i in range(n * m):
        parent[i] = i
    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                v = i * m + j % m
                dfs(i, j, v)
    print(ans)