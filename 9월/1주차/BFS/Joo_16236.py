from typing import *
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]
baby_size = 2
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            baby_row, baby_col = i, j


def bfs(baby_row: int, baby_col: int, baby_size: int):
    discovered = [[0]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append([baby_row, baby_col])
    discovered[baby_row][baby_col] = 1
    tmp = []
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] <= baby_size and discovered[nr][nc] == 0:
                queue.append([nr, nc])
                discovered[nr][nc] = 1
                distance[nr][nc] = distance[r][c] + 1
                if graph[nr][nc] < baby_size and graph[nr][nc] != 0:
                    tmp.append([nr, nc, distance[nr][nc]])

    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))

cnt = 0
res = 0
while True:
    fish = bfs(baby_row, baby_col, baby_size)
    if len(fish) == 0:
        break
    nr, nc, dis = fish.pop()
    res += dis
    graph[baby_row][baby_col], graph[nr][nc] = 0, 0
    baby_row, baby_col = nr, nc
    cnt += 1
    if cnt == baby_size:
        baby_size += 1
        cnt = 0
print(res)