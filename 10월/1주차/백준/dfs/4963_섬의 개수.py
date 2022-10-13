import sys
from collections import deque
sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

dr = [-1, -1, -1, 1, 1, 1, 0, 0]
dc = [-1, 1, 0, -1, 1, 0, -1, 1]

def dfs(r: int, c: int):
    visited[r][c] = 1
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < h and 0 <= nc < w:
            if graph[nr][nc] == 1 and not visited[nr][nc]:
                dfs(nr, nc)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)