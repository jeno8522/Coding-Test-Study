import sys
from collections import deque

input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(startR, startC):
    q = deque()
    q.append((startR, startC))
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr,nc))
    res.append(cnt)

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
res = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

res.sort()
print(len(res))
for e in res:
    print(e)