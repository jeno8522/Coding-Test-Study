from typing import *
from collections import deque
import sys                      #dfs 최대 재귀호출 수 제한
sys.setrecursionlimit(100000)

def marking(rect: list):            #직사각형 마킹하기

    for i in range(rect[1], rect[3]):
        for j in range(rect[0], rect[2]):
            if graph[i][j] == 0:
                graph[i][j] = 1

def dfs(r: int, c: int) -> int:
    global cnt          #cnt 전역변수 선언
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    graph[r][c] = 1
    for i in range(4):      #일단 네개 포문
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < m and 0 <= nc < n:     #dfs 시작 지점이 조건 충족 시 상하좌우 dfs 재귀호출
            if graph[nr][nc] == 0:
                cnt += 1
                dfs(nr, nc)





m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
rects = [list(map(int, input().split())) for _ in range(k)]
areas = []
area = 0
cnt = 1

for i in range(k):
    marking(rects[i])

# for i in graph:
#     print(i)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:    #마킹 안된부분 dfs 실시 (area, cnt 카운트)
            area += 1
            dfs(i, j)
            areas.append(cnt)
            cnt = 1

# for i in graph:
#     print(i)
print(area)
print(*sorted(areas))   #리스트 요소 출력

