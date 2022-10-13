from collections import deque
import heapq

def bfs(r: int, c: int):
    q = deque()
    q.append((r, c))
    crashed[r][c] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if crashed[nr][nc] == -1:   #첫 방문 일때
                    if graph[nr][nc] == 0:  #벽을 안 부수고 지나가는 거면 q에 우선순위로 appendleft
                        q.appendleft((nr, nc))
                        crashed[nr][nc] = crashed[r][c]
                    else:
                        q.append((nr, nc))  #벽을 부수고 지나가는 거면 q에 그냥 append
                        crashed[nr][nc] = crashed[r][c] + 1
            # print(visited)
            # print(crashed)

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
# print(graph)
crashed = [[-1]*m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

bfs(0, 0)


print(crashed[-1][-1])
