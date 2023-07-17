import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check_boundary(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs(r, c):
    global numbering

    q = deque()
    tmp = []
    q.append((r, c))
    tmp.append((r,c))

    visited[r][c] = True
    cnt = 1
    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]
            if not check_boundary(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if graph[nr][nc] > 0:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
            tmp.append((nr, nc))
            cnt += 1

    for pos in tmp:
        label[pos[0]][pos[1]] = [cnt, numbering]
    numbering+=1




if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    pos = []
    label = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    numbering = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and not visited[i][j]:
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                val = 0
                tmp = set()
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if not check_boundary(nr, nc):
                        continue
                    if graph[nr][nc] != 0:
                        continue
                    if label[nr][nc][1] in tmp:
                        continue
                    val += label[nr][nc][0]
                    tmp.add(label[nr][nc][1])
                graph[i][j] += val


    # for line in label:
    #     print(*line, sep='')
    # print()
    for line in graph:
        for e in line:
            print(e%10, sep='', end='')
        print()