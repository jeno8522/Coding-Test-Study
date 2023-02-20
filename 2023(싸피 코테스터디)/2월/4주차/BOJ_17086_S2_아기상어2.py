import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, -1, 1, 1, -1, 1, 0, 0]
dc = [1, -1, 1, -1, 0, 0, 1, -1]


def bfs(startR, startC, start_cnt):
    global safe
    q = deque()
    visited[startR][startC] = 1
    q.append((startR, startC, start_cnt))
    while q:
        r, c, cnt = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if graph[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc, cnt + 1))
                else:
                    safe = max(safe, cnt)
                    return
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

safe = -1

for i in range(N):
    for j in range(M):
        if graph[i][j] != 1:
            visited = [[0] * M for _ in range(N)]
            bfs(i, j, 1)
print(safe)
