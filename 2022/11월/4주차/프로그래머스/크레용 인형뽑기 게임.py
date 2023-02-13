from collections import deque

def solution(board, moves):
    answer = 0
    tmp = list(zip(*board))
    t_board = [list(x) for x in tmp]
    q = deque()
    for idx in moves:
        for i in range(len(t_board[idx - 1])):
            if t_board[idx - 1][i] != 0:
                q.append(t_board[idx - 1][i])
                if len(q) >= 2:
                    if q[-1] == q[-2]:
                        answer += 2
                        q.pop()
                        q.pop()
                t_board[idx - 1][i] = 0
                break


    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))