from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    p = deque()
    for idx, val in enumerate(priorities):
        p.append((idx, val))
    max = 0
    n = len(priorities)
    cnt = 0
    idx = location
    res = []

    while p:
        idx -= 1
        e = p.popleft()
        q.append(e)

        if e[1] > max:
            max = e[1]
            while q[0][1] < max:
                p.append(q.popleft())
        if not p:
            print = q.popleft()
            cnt += 1
            max = 0
            if print[0] == location:
                answer = cnt
                break
            while q:
                p.append(q.popleft())




    return answer

priorities = [1, 1, 9, 1, 1, 1]

print(solution(priorities, 0))