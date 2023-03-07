import sys
from collections import deque
input = sys.stdin.readline

def count_score(team):
    turn = 0
    score = 0
    for i in range(N):
        b1, b2, b3 = 0, 0, 0
        out_cnt = 0
        while out_cnt < 3:
            if ta_info[i][team[turn]] == 0:
                out_cnt += 1
            elif ta_info[i][team[turn]] == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif ta_info[i][team[turn]] == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif ta_info[i][team[turn]] == 3:
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            elif ta_info[i][team[turn]] == 4:
                score += b3 + b2 + b1 + 1
                b3, b2, b1 = 0, 0, 0
            turn = (turn + 1) % 9
    return score

def permutation(cnt):
    global ans
    if cnt == 9:
        game_result = count_score(team)
        if ans < game_result:
            ans = game_result
        return
    if cnt == 3:
        permutation(cnt+1)
        return
    for i in range(9):
        if visited[i]: continue
        team[cnt] = i
        visited[i] = 1
        permutation(cnt + 1)
        visited[i] = 0


ans = 0
N = int(input().rstrip())
ta_info = [list(map(int, input().split())) for _ in range(N)]

team = [0] * 9
team[3] = 0

visited = [0] * 9
visited[0] = 1

permutation(0)
print(ans)


