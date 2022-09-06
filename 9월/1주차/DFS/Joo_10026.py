from typing import *
from collections import deque
import sys                      #dfs 최대 재귀호출 수 제한
sys.setrecursionlimit(100000)

def dfs(r: int, c: int):
    visited[r][c] = 1       #방문 시 visited 값 1로 마킹
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:    #조건 충족 시 dfs
            if graph[r][c] == graph[nr][nc]:
                dfs(nr, nc)

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]         #dfs, bfs 에서 visited 개념 적극 사용
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt_not_RGB = 0
cnt_RGB = 0




for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:      #방문한 적 없으면 dfs 수행 -> 같은 지역 순회
            dfs(i, j)
            cnt_not_RGB += 1

visited = [[0]*n for _ in range(n)]     #visited 0으로 초기화

for i in range(n):                  # for 적록색약, G를 R로 다바꿈
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):                  #위와 동일하게 dfs 수행
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt_RGB += 1

print(cnt_not_RGB, cnt_RGB)
