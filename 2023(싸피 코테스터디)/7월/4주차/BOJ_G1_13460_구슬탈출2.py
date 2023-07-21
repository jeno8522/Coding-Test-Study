import sys

input = sys.stdin.readline

# U, D, L, R
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#벽인지, 골인지, 빈곳인지
def check(r, c):
    if graph[r][c] == '#':  #벽
        return 0
    elif graph[r][c] == 'O': #골
        return 1
    # else:                    #빈곳
    #     return 2
def move(ball, r, c, d):
    nr, nc = r, c
    while True:
        nr += dr[d]
        nc += dc[d]
        now = check(nr, nc)
        if now == 0:    # 다음이 벽이면
            break
        elif now == 1:  # 다음이 골이면
            return True
        ball = [nr, nc]
    return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]
    rPos, bPos, gPos = [-1, -1], [-1, -1], [-1, -1]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rPos = [i, j]
            elif graph[i][j] == 'B':
                bPos = [i, j]
            elif graph[i][j] == 'O':
                gPos = [i, j]

    for _ in range(10):
        rTmp, bTmp = rPos[:], bPos[:]
        for i in range(4):

