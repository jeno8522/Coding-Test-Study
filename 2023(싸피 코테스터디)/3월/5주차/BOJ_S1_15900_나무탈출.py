import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    global total
    q = deque()
    q.append((1, 0))
    visited[1] = 1
    while q:
        now, w = q.popleft()
        visited[now] = 1
        isLeaf = True
        for next in graph[now]:
            if visited[next]:
                continue
            isLeaf = False
            visited[next] = 1
            q.append((next, w + 1))
        if isLeaf:
            total += w


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
total = 0
for _ in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
bfs()
# print(total)
if total % 2 == 1:
    print("Yes")
else:
    print("No")
