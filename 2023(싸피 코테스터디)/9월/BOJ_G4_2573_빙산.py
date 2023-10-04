import sys
from collections import deque



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check_boundary(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs(startR, startC):
    q = deque()
    q.append((startR, startC))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not check_boundary(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if graph[nr][nc] == 0:
                q.append((nr, nc))
            if graph[nr][nc] > 0:
                ices.append((nr, nc))
            visited[nr][nc] = True

def melting():
    cnts = []
    # print("ices == " , ices)
    for ice in ices:
        cnt = 0
        for i in range(4):
            nr = ice[0] + dr[i]
            nc = ice[1] + dc[i]
            if not check_boundary(nr, nc):
                continue
            if graph[nr][nc] == 0:
                cnt += 1
        cnts.append(cnt)
    # print("cnts == " , cnts)
    for i in range(len(ices)):

        graph[ices[i][0]][ices[i][1]] -= cnts[i]
        if graph[ices[i][0]][ices[i][1]] < 0:
            graph[ices[i][0]][ices[i][1]] = 0

def count_island(startR, startC):
    q = deque()
    q.append((startR, startC))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not check_boundary(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if graph[nr][nc] > 0:
                q.append((nr, nc))
            visited[nr][nc] = True

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    while True:
        result += 1
        visited = [[False] * m for _ in range(n)]
        ices = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0 and not visited[i][j]:
                    bfs(i, j)
        melting()
        # print(*graph, sep='\n')
        # print()

        visited = [[False] * m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0 and not visited[i][j]:
                    count_island(i, j)
                    # print(i, j)
                    cnt += 1
        if cnt >= 2 or cnt == 0:
            break
    if cnt == 0:
        result = 0
    print(result)