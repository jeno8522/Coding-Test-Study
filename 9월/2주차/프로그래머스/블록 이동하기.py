from typing import *
from collections import deque

def solution(board):
    answer = 0
    visited = [[0] * len(board) for _ in range(len(board))]
    time_cnt = []
    que = deque([0,0,0,1])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def move_robot(r1: int, c1: int, r2: int, c2: int):
        can_move = []
        for i in range(4):
            nr1, nr2 = r1 + dr[i], r2 + dr[i]
            nc1, nc2 = c1 + dc[i], c2 + dc[i]
            if 0 <= nr1 < len(board) and \
                0 <= nr2 < len(board) and \
                0 <= nc1 < len(board) and \
                0 <= nc2 < len(board):
                if visited[nr1][nc1] == 0 and \
                    visited[nr2][nc2] == 0 and \
                    board[nr1][nc1] == 0 and \
                    board[nr2][nc2] == 0:
                    can_move.append([nr1,nc1,nr2,nc2])
        for i in range(4):
            can_move.append(rotate(nr1,nc1,nr2,nc2,True))
        for i in range(4):
            can_move.append(rotate(nr1,nc1,nr2,nc2,False))
        return can_move
    while que:
        r1, c1, r2, c2 = que.popleft()


def rotate(nr1: int, nc1: int, nr2: int, nc2: int, is_main: bool) -> int:
    if is_main:
        main_r, main_c = nr1, nc1
        sub_r, sub_c = nr2, nc2
    else :
        main_r, main_c = nr2, nc2
        sub_r, sub_c = nr1, nc1
    if main_r == sub_r:
        if main_c > sub_c:
            nr2 = main_r + 1
            nc2 = main_c
        else:
            nr2 = main_r - 1
            nc2 = main_c
    elif main_c == sub_c:
        if main_r > sub_r:
            nr2 = main_r
            nc2 = main_c - 1
        else:
            nr2 = main_r
            nc2 = main_c + 1
    return nr1, nc1, nr2, nc2


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))

# # 파이썬
# from collections import deque
#
#
# def can_move(cur1, cur2, new_board):
#     Y, X = 0, 1
#     cand = []
#     # 평행이동
#     DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#     for dy, dx in DELTAS:
#         nxt1 = (cur1[Y] + dy, cur1[X] + dx)
#         nxt2 = (cur2[Y] + dy, cur2[X] + dx)
#         if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
#             cand.append((nxt1, nxt2))
#     # 회전
#     if cur1[Y] == cur2[Y]:  # 가로방향 일 때
#         UP, DOWN = -1, 1
#         for d in [UP, DOWN]:
#             if new_board[cur1[Y] + d][cur1[X]] == 0 and new_board[cur2[Y] + d][cur2[X]] == 0:
#                 cand.append((cur1, (cur1[Y] + d, cur1[X])))
#                 cand.append((cur2, (cur2[Y] + d, cur2[X])))
#     else:  # 세로 방향 일 때
#         LEFT, RIGHT = -1, 1
#         for d in [LEFT, RIGHT]:
#             if new_board[cur1[Y]][cur1[X] + d] == 0 and new_board[cur2[Y]][cur2[X] + d] == 0:
#                 cand.append(((cur1[Y], cur1[X] + d), cur1))
#                 cand.append(((cur2[Y], cur2[X] + d), cur2))
#
#     return cand
#
#
# def solution(board):
#     # board 외벽 둘러싸기
#     N = len(board)
#     new_board = [[1] * (N + 2) for _ in range(N + 2)]
#     for i in range(N):
#         for j in range(N):
#             new_board[i + 1][j + 1] = board[i][j]
#
#     # 현재 좌표 위치 큐 삽입, 확인용 set
#     que = deque([((1, 1), (1, 2), 0)])
#     confirm = set([((1, 1), (1, 2))])
#
#     while que:
#         cur1, cur2, count = que.popleft()
#         if cur1 == (N, N) or cur2 == (N, N):
#             return count
#         for nxt in can_move(cur1, cur2, new_board):
#             if nxt not in confirm:
#                 que.append((*nxt, count + 1))
#                 confirm.add(nxt)