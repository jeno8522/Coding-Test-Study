dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check_boundary(r, c):
    return 0 <= r < 101 and 0 <= c < 101


def isDoolle(r, c):
    tmp = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if check_boundary(nr, nc):
            if graph[nr][nc]:
                tmp += 1
    return tmp


n = int(input())
graph = [[False] * 101 for _ in range(101)]
for _ in range(n):
    c, r = map(int, input().split())
    for i in range(r, r + 10):
        for j in range(c, c + 10):
            graph[i][j] = True

cnt = 0
for i in range(101):
    for j in range(101):
        if not graph[i][j]:
            cnt += isDoolle(i, j)

print(cnt)
