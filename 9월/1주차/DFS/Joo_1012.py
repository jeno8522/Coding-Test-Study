from typing import *
from collections import deque
import sys
sys.setrecursionlimit(10000)

def dfs(r:int, c:int):
    if r<0 or r>=n or c<0 or c>=m:
        return
    if graph[r][c] != 1:
        return
    if 0<=r<n and 0<=c<m:
        if graph[r][c] == 1:
            graph[r][c] = 2

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    baechoo = deque()
    cnt = 0

    for j in range(k):
        c, r = map(int, input().split())
        graph[r][c] = 1
        baechoo.append([r, c])

    while baechoo:
        r, c = baechoo.popleft()
        if graph[r][c] == 1:
            dfs(r,c)
            cnt += 1
    # for x in range(n):
    #     for y in range(m):
    #         if graph[x][y] == 1:
    #             dfs(x, y)
    #             cnt += 1


    print(cnt)
