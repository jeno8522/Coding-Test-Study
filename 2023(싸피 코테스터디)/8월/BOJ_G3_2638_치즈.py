import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check_boundary(r, c):
    return 0 <= r < n and 0 <= c < m

def check_around(r, c, visited):
    cnt = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not check_boundary(nr, nc):
            continue
        if not graph[nr][nc] and visited[nr][nc]:
            cnt += 1
    if cnt >= 2:
        return True
    return False

def bfs():
    q = deque()
    visited = [[False] * m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = True
    around = []
    isFinished = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not check_boundary(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if graph[nr][nc]:
                isFinished = False
                visited[nr][nc] = True
                around.append((nr, nc))
            else:
                visited[nr][nc] = True
                q.append((nr,nc))

    remove = []
    for point in around:
        if check_around(point[0], point[1], visited):
            remove.append((point[0], point[1]))
    for point in remove:
        graph[point[0]][point[1]] = 0
    return isFinished




if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    while not bfs():
        # print(*graph, sep='\n')
        result += 1
    print(result)