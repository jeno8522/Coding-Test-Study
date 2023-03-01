import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def bfs(r, c):
    fish = []
    visited[r][c] = 1
    q = deque()
    q.append((r, c, 0))
    while q:
        nowR, nowC, nowDis = q.popleft()
        for i in range(4):
            nr = nowR + dr[i]
            nc = nowC + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if size < graph[nr][nc] or visited[nr][nc]:
                continue
            if graph[nr][nc] == 0 or size == graph[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc, nowDis + 1))
            elif size > graph[nr][nc]:
                fish.append([nr, nc, nowDis + 1])
    fish = sorted(fish, key=lambda x: (x[2], x[0], x[1]))
    return fish


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
startR = startC = -1
size = 2
result = 0

for i in range(N):
    find = False
    for j in range(N):
        if graph[i][j] == 9:
            startR, startC = i, j
            graph[i][j] = 0
            find = True
            break
    if find:
        break

eatCnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    fishes = bfs(startR, startC)
    # print(fishes)
    eatCnt += 1
    if not fishes:
        break
    fish_info = fishes[0]
    result += fish_info[2]
    startR = fish_info[0]
    startC = fish_info[1]
    graph[startR][startC] = 0
    if eatCnt == size:
        size += 1
        eatCnt = 0

print(result)
