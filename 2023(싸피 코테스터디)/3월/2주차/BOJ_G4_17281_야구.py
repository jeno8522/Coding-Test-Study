import sys
from collections import deque
input = sys.stdin.readline

def count_score(team):
    turn = 0
    score = 0
    for i in range(N):
        b1, b2, b3 = 0, 0, 0    # 초기 : deque 사용 -> 시간초과로 1,2,3루 변수를 두어서 시간 줄임
        out_cnt = 0
        while out_cnt < 3:
            if ta_info[i][team[turn]] == 0:     # 편하게 따로 변수에 값을 넣어서 사용하지 않고 바로 접근
                out_cnt += 1
            elif ta_info[i][team[turn]] == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif ta_info[i][team[turn]] == 2:
                score += b3 + b2                # 1,2,3루 변수를 두어서 score에 해당 변수를 바로 더해줄 수 있음
                b3, b2, b1 = b1, 1, 0           # ex) 2루타일 때, 2 3루 주자의 변수를 바로 score에 더해주고 각 루를 초기화 해줌
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
    if cnt == 9:        # 9번 타자 까지 뽑으면 해당 타순으로 이닝 진행 후 점수의 최댓값 갱신
        game_result = count_score(team)
        if ans < game_result:
            ans = game_result
        return
    if cnt == 3:            # 4번 타자 뽑을 때 그냥 다음 재귀호출
        permutation(cnt+1)
        return
    for i in range(9):      # 순열
        if visited[i]: continue
        team[cnt] = i
        visited[i] = 1
        permutation(cnt + 1)
        visited[i] = 0


ans = 0
N = int(input().rstrip())
ta_info = [list(map(int, input().split())) for _ in range(N)]

team = [0] * 9
team[3] = 0     # 4번 타자에 1번 선수 지정

visited = [0] * 9
visited[0] = 1  # 4번 타자를 미리 visited check 해줌

permutation(0)
print(ans)
