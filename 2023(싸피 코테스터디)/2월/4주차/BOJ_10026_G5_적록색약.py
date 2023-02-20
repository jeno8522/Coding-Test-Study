import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(color, startR, startC):
    q = deque()
    q.append((startR, startC))
    while q:
        r, c = q.popleft()
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == color and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))


def bfs_weakness(color, startR, startC):
    q = deque()
    q.append((startR, startC))
    isColorRG = False
    if color == "R" or color == "G":
        isColorRG = True
    while q:
        r, c = q.popleft()
        visited_weakness[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited_weakness[nr][nc]:
                    if isColorRG and graph[nr][nc] != "B":
                        visited_weakness[nr][nc] = 1
                        q.append((nr, nc))
                    elif graph[nr][nc] == color:
                        visited_weakness[nr][nc] = 1
                        q.append((nr, nc))

input = sys.stdin.readline
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited_weakness = [[0] * N for _ in range(N)]
cnt = 0
cnt_weakness = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(graph[i][j],i, j)
            cnt += 1
        if not visited_weakness[i][j]:
            bfs_weakness(graph[i][j],i,j)
            cnt_weakness += 1
print(cnt, cnt_weakness)
