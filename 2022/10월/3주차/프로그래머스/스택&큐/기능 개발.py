import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()

    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))

    max = days.popleft()
    cnt = 1
    while days:
        day = days.popleft()
        if day > max:
            answer.append(cnt)
            cnt = 1
            max = day
            if not days:
                break
        else: cnt += 1

    if cnt > 0: answer.append(cnt)

    return answer


progresses = [1,1,50]
speeds = [100,2,1]

print(solution(progresses, speeds))