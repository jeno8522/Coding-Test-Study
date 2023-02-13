import sys
sys.stdin = open("input.txt", "r")
def flip(r, c, color):  #반대 쪽에 놓인 color, 그 반대랑 같은 color
    dr = [-1, 1, 0, 0, -1, 1, -1, 1]
    dc = [0, 0, -1, 1, -1, 1, 1, -1]
    if color == 1:
        o_color = 2
    elif color == 2:
        o_color = 1
    for k in range(8):
        isValid = True
        nr = r
        nc = c
        tmp = []
        while True:
            nr += dr[k]
            nc += dc[k]
            if 1 > nr or nr > n or 1 > nc or nc > n or board[nr][nc] == 0:
                break
            if board[nr][nc] == color:              #같은 색이면 break
                for q in tmp:
                    board[q[0]][q[1]] = color
                break
            if board[nr][nc] == o_color:                                   #다른 색이면 추가
                tmp.append([nr, nc])






T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * (n+1) for _ in range(n+1)]
    board[n//2][n//2], board[n//2 + 1][n//2 + 1] = 2, 2
    board[n//2][n//2 + 1], board[n//2 + 1][n//2] = 1, 1
    # board = [[0, 0, 0, 0, 0],
    #          [0, 2, 1, 0, 0],
    #          [0, 1, 1, 1, 0],
    #          [0, 0, 1, 2, 1],
    #          [0, 0, 0, 0, 2]]
    #
    # for e in board:
    #     print(e)
    # print()
    for i in range(m):
        y, x, color = map(int, input().split())
        board[x][y] = color
        flip(x, y, color)
        # for l in board:
        #     print(l)
        # print()

    w, b = 0, 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] == 1:
                b += 1
            elif board[i][j] == 2:
                w += 1
    print(f'#{test_case} {b} {w}')