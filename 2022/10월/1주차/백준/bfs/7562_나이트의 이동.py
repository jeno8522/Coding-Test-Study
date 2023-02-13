import sys
from collections import deque
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dr = [-1, -1, 1, 1, -2, -2, 2, 2]
dc = [-2, 2, -2, 2, -1, 1, -1, 1]

def bfs():
    while q:
        r, c = q.popleft()
        if r == end_r and c == end_c:
            print(graph[r][c])
            return
        visited[r][c] = 1
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    graph[nr][nc] = graph[r][c] + 1
                    q.append((nr, nc))


t = int(input())
for _ in range(t):
    n = int(input())
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    visited = [[0] * n for _ in range(n)]
    graph = [[0] * n for _ in range(n)]
    q = deque()
    q.append((start_r, start_c))
    bfs()


