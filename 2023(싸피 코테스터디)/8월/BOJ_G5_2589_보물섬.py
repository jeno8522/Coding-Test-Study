import sys
from collections import deque
input = sys.stdin.readline


dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(startR, startC):
    global result
    q = deque()
    visited = [[False] * m for _ in range(n)]
    q.append((startR, startC, 0))
    visited[startR][startC] = True

    tmpMax = -1
    while q:
        r, c, v = q.popleft()
        tmpMax = max(tmpMax, v)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if visited[nr][nc]:
                continue
            if graph[nr][nc] == 'W':
                continue
            visited[nr][nc] = True
            q.append((nr, nc, v+1))

    result = max(result, tmpMax)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    result = 1
    # print(*graph, sep='\n')

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L':
                bfs(i, j)
    print(result)