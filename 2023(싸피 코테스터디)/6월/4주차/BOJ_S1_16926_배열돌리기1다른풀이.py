import sys
from collections import deque

input = sys.stdin.readline


def check_boundary(r, c, d):
    return d <= r < n - d and d <= c < m - d


n, m, rotate = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
depth = min(n, m) // 2

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for d in range(depth):
    q = deque()
    r = 0 + d
    c = 0 + d
    for dr, dc in dir:
        while True:
            nr = r + dr
            nc = c + dc
            if check_boundary(nr, nc, d):
                q.append(graph[nr][nc])
                r, c = nr, nc
            else:
                break
    # print(q)
    for _ in range(rotate):
        q.append(q.popleft())
    # print(q)
    r = 0 + d
    c = 0 + d
    for dr, dc in dir:
        while True:
            nr = r + dr
            nc = c + dc
            if check_boundary(nr, nc, d):
                graph[nr][nc] = q.popleft()
                r, c = nr, nc
            else:
                break

for line in graph:
    print(*line)