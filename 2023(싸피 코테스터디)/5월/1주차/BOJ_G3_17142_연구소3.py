import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def check_boundary(r, c):
    return 0 <= r < N and 0 <= c < N

def recover():
    for i in range(N):
        graph[i] = save[i][:]

def get_max():
    tmp = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                return -1
            if save[i][j] == -1:
                continue
            tmp = max(tmp, graph[i][j])
    return tmp

def bfs(virus_pos):
    q = deque()
    for e in virus_pos:
        q.append(e)
        graph[e[0]][e[1]] = 1
    while q:
        r, c = q.popleft()
        w = graph[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not check_boundary(nr, nc):
                continue
            if graph[nr][nc] == 0 or graph[nr][nc] == -1:
                graph[nr][nc] = w + 1
                q.append([nr, nc])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
save = []

minValue = sys.maxsize

virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append([i, j])
            graph[i][j] = -1
        if graph[i][j] == 1:
            graph[i][j] = -2

for line in graph:
    save.append(line[:])

if get_max() > -1:
    print(0)
    exit(0)

isValid = False
for combi in combinations(virus, M):
    bfs(combi)
    local_max = get_max()
    recover()
    if local_max > -1:
        isValid = True
    else:
        continue
    minValue = min(minValue, local_max)

if isValid:
    print(minValue - 1)
else:
    print(-1)
