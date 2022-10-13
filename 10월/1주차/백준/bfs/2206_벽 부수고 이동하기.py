import sys
from collections import deque
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r: int, start_c: int, isWallCrashed: int):
    q = deque()
    q.append((start_r, start_c, isWallCrashed))
    while q:
        r, c, isW = q.popleft()
        if r == n - 1 and c == m - 1:
            return visited[r][c][isW]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 1 and isW == 0: #다음이 벽이고 벽 부수기 찬스를 아직 쓰지 않았다면
                    visited[nr][nc][1] = visited[r][c][0] + 1    #벽 부수기 찬스 쓴 visited에, 아직 안 쓴 전 visited 값 + 1 삽입
                    q.append((nr, nc, 1))   #벽 부수기 찬스 쓴 nr, nc append
                elif graph[nr][nc] == 0 and not visited[nr][nc][isW]:   #다음이 벽이 아니고 방문한 적이 없다면(벽 부수기 찬스를 썼던 안 썼던)
                    visited[nr][nc][isW] = visited[r][c][isW] + 1 #visited에 전 visitied 값 + 1 삽입
                    q.append((nr, nc, isW)) #nr, nc, 벽 부수기 찬스 유무 삽입
    return -1


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0], visited[0][0][1] = 1, 1

print(bfs(0, 0, 0))