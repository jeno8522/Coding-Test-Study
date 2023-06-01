import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def check_boundary(z, x, y):
    return 0 <= x < n and 0 <= y < m and 0 <= z < h


def bfs(z, x, y):

    q = deque()
    q.append((z,x,y, 2))
    tomatos[z][x][y] = 2
    while q:
        # for lines in tomatos:
        #     for line in lines:
        #         print(line)
        #     print()
        now = q.popleft()
        for i in range(6):
            nz = now[0] + dz[i]
            nx = now[1] + dx[i]
            ny = now[2] + dy[i]
            if not check_boundary(nz, nx, ny):
                continue
            if tomatos[nz][nx][ny] == 1 or tomatos[nz][nx][ny] == -1:
                continue
            if tomatos[nz][nx][ny] > now[3] + 1 or tomatos[nz][nx][ny] == 0:
                tomatos[nz][nx][ny] = now[3] + 1
                q.append((nz,nx,ny, now[3] + 1))


def check_finished():
    global result
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomatos[k][i][j] == 0:
                    result = -1
                    return False
                result = max(result, tomatos[k][i][j] - 2)
    return True


if __name__ == "__main__":
    m, n, h = map(int, input().split())

    # print(n, m, h)
    tomatos = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    for k in range(h):
        for i in range(n):
            for j in range(m):

                if tomatos[k][i][j] == 1:
                    bfs(k, i, j)
    result = -1
    check_finished()
    print(result)
