import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
tmp = list(map(int, input().split()))
q = deque()
for e in tmp:
    q.append([e, 0])

durCnt = 0
stage = 1
while True:
    q.appendleft(q.pop())
    q[N - 1][1] = 0  # 내리는 위치에서 로봇 내림
    isFinished = False
    for now in range(N - 2, -1, -1):
        if q[now][1] == 1:  # 로봇이 있는 칸이면
            if q[now+1][0] == 0 or q[now+1][1] == 1:  # 로봇이 이동할 다음 칸의 내구도가 0이면 그냥 가만히 있음, 다음 칸에 로봇이 있으면 가만히 있음
                continue
            q[now][1] -= 1      # now 로봇 빼주고
            q[now+1][1] += 1    # 다음 칸 로봇 더해줌
            q[now+1][0] -= 1  # 다음 칸 내구도 -1
            if q[now+1][0] == 0:  # 다음 칸 내구도가 0이 되면 count 해줌
                durCnt += 1
                if durCnt == K:
                    isFinished = True
                    break
    if isFinished:
        break
    q[N - 1][1] = 0    # 내리는 위치에서 로봇 내림
    if q[0][0] > 0 and q[0][1] == 0:  # 올리는 위치의 내구도가 0이상, 로봇이 안 올라가져 있을 때
        q[0][0] -= 1
        q[0][1] = 1
        if q[0][0] == 0:
            durCnt += 1
            if durCnt == K:
                break
    stage += 1
print(stage)