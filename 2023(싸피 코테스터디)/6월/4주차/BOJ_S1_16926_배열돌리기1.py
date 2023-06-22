import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
depth = min(n, m) // 2
q = deque()

for d in range(depth):
    for i in range(m - 2 * d):
        c = i + d
        q.append(graph[d][c])
    for i in range(d + 1, n - (d + 1)):
        c = m - 1 - d
        q.append(graph[i][c])
    for i in range(m - 2 * d):
        c = m - 1 - (i + d)
        q.append(graph[n - 1 - d][c])
    for i in range(d + 1, n - (d + 1)):
        c = d
        q.append(graph[n - 1 - i][c])
    # print(q)
    for _ in range(r):
        q.append(q.popleft())

    for i in range(m - 2 * d):
        c = i + d
        graph[d][c] = q.popleft()
    for i in range(d + 1, n - (d + 1)):
        c = m - 1 - d
        graph[i][c] = q.popleft()
    for i in range(m - 2 * d):
        c = m - 1 - (i + d)
        graph[n - 1 - d][c] = q.popleft()
    for i in range(d + 1, n - (d + 1)):
        c = d
        graph[n - 1 - i][c] = q.popleft()

for line in graph:
    print(*line)
