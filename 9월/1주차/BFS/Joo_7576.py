from typing import *
from collections import deque

m, n = map(int, input().split())
graph = []

# graph = [list(map(int, input().split())) for i in range(n)]
# graph 입력 짧은 줄

for i in range(n):
    tomatos = list(map(int, input().split()))
    graph.append(tomatos)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()     #시간초과 떠서 queue의 pop(0)은 O(N), deque의 popleft는 O(1)이므로 deque 사용

count_days = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j]) #미리 1인 지점 큐에 저장


def bfs():  #주변, 최소 -> bfs
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            moved_x = x + dx[i]
            moved_y = y + dy[i]
            if 0 <= moved_x < n and 0 <= moved_y < m and graph[moved_x][moved_y] == 0:
                graph[moved_x][moved_y] = graph[x][y] + 1   #원래지점의 사방 중 0인 지점을 원래지점 + 1로 변경 -> 익는 일자가 고정됨
                queue.append([moved_x, moved_y])

bfs()
for line in graph:
    if 0 in line:   # bfs 후 0이 있다는 것은 -1에 의해 다 안익는 다는 것
        print(-1)
        exit(0)

    count_days = max(count_days, max(line)) #저장된 일자 중 가장 큰 값

print(count_days - 1)   #시작이 1이므로


