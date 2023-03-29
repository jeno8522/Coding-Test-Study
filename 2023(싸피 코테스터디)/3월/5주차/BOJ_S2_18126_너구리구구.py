import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global max_dis
    q = deque()
    q.append((1,0))
    visited[1] = 1
    while q:
        now, now_w = q.popleft()
        for e in graph[now]:
            next, next_w = e[0], e[1]
            if visited[next]:
                continue
            visited[next] = 1
            max_dis = max(max_dis, now_w + next_w)
            q.append((next, now_w + next_w))



n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
max_dis = 0
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

bfs()
print(max_dis)