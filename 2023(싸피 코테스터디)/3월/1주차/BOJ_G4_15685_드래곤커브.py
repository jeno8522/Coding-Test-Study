import sys

input = sys.stdin.readline

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def check_square(r, c):
    cr = [1, 1, 0]
    cc = [0, 1, 1]
    for i in range(3):
        nr = r + cr[i]
        nc = c + cc[i]
        if graph[nr][nc] == 0:
            return False
    return True


graph = [[0] * 101 for _ in range(101)]
N = int(input())

for _ in range(N):
    c, r, d, g = map(int, input().split())
    move_info = [d]
    for i in range(g):
        tmp = []
        for j in range(len(move_info)-1, -1, -1):
            dIdx = move_info[j] + 1
            if dIdx == 4:
                dIdx = 0
            tmp.append(dIdx)
        move_info += tmp
    graph[r][c] = 1
    for move in move_info:
        r += dr[move]
        c += dc[move]
        graph[r][c] = 1

res = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            if check_square(i, j):
                res += 1

print(res)