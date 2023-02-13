from collections import deque
def solution(board, skill):
    answer = 0
    #어떤 면적에 특정 값을 더하거나 뺄때 효율성을 위한 누적합 사용
    sum_map = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]    #누적합 리스트

    #주어진 범위보다 한칸 뒤에 누적합을 위한 값을 넣는다.
    #N 0 0 -N
    #0 0 0 0    ->   (0, 0) ~ (2, 2) 범위에 N을 넣기 위한 누적합 map
    #0 0 0 0
    #-N 0 0 N
    for type, r1, c1, r2, c2, degree in skill:
        sum_map[r1][c1] += degree if type == 2 else -degree
        sum_map[r1][c2 + 1] -= degree if type == 2 else degree
        sum_map[r2 + 1][c1] -= degree if type == 2 else degree
        sum_map[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    #행 기준 누적합
    #N N N 0
    #0 0 0 0
    #0 0 0 0
    #-N-N-N 0

    for i in range(len(sum_map) - 1):
        for j in range(len(sum_map[0]) - 1):
            sum_map[i][j + 1] += sum_map[i][j]

    #열 기준 누적합
    #N N N 0
    #N N N 0     ->  (0, 0) ~ (2, 2) 범위에 N만큼의 변화
    #N N N 0
    #0 0 0 0
    for j in range(len(sum_map[0]) - 1):
        for i in range(len(sum_map) - 1):
            sum_map[i + 1][j] += sum_map[i][j]

    # 기존에 주어진 board에 누적합 결과를 더함
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += sum_map[i][j]
            #파괴되지 않은 건물 count
            if board[i][j] > 0:
                answer += 1

    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

a = [[1,2,3],[4,5,6],[7,8,9]]
b = 	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

# print(solution(board, skill))
print(solution(a,b))