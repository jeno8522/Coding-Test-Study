from collections import deque
import numpy

def solution(source):
    q = deque()
    for c in source:
        q.append(c)
    answer = ''

    while True:
        tmp = ''
        q_len = len(q)
        if q_len == 1:
            answer += q.popleft()
            break
        for i in range(q_len):
            c = q.popleft()
            if not c in tmp:
                tmp += c
            else:
                q.append(c)
        answer += ''.join(sorted(tmp))
    return answer

print(solution('cucumber'))