import sys
sys.setrecursionlimit(10001)
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r: int, c: int, num: int):  # 섬 구분하기
    graph[r][c] = num
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if not visited[nr][nc]:
                if graph[nr][nc] == 1:
                    graph[nr][nc] = num
                    visited[nr][nc] = 1
                    dfs(nr, nc, num)
                else:
                    visited[nr][nc] = 1     #그래프가 0일때, 해당 구역을 미리 배열에 담아서 후에 bfs 수행
                    edges.add((nr, nc))

def bfs(x:int, y:int, num:int):  #최단 경로 다리 찾기 위함
    if graph[x][y] != 0:
        return 0
    visited = [[0] * n for _ in range(n)]
    q = deque([(x,y,1)])
    visited[x][y] = 1
    while q:
        r, c, dis = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    if graph[nr][nc] == 0:  #바다면 거리 + 1
                        q.append((nr,nc,dis+1))
                    elif graph[nr][nc] != num:  #다른 섬이면 바로 해당 거리 return
                        return dis
    return 10 ** 7  #다른 섬을 못 찾으면 max값 return

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
edges_res = []
num = 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            edges = set()   #해당 섬의 바다와 닿아있는 포인트를 set에 저장
            dfs(i, j, num)
            edges_res.append(list(edges))   #섬 별로 체크포인트들을 배열에 append
            num += 1

result = 10**7
for idx in range(len(edges_res)):
    for i,j in edges_res[idx]:  #저장된 섬 별 체크포인트 bfs 수행
        distance = bfs(i, j, idx+2)
        if result > distance:
            result = distance
print(result)