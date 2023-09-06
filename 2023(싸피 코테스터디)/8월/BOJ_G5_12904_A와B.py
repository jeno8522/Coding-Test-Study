import sys
from collections import deque

input = sys.stdin.readline

def remove_char(str):
    global q
    cnt = 0
    if str[-1] == 'A':
        cnt += 1
        q.append(str[:-1])
    if str[0] == 'B':
        cnt += 1
        tmp = str[1:]
        q.append(tmp[::-1])
    return cnt



if __name__ == '__main__':
    S = input().rstrip()
    T = input().rstrip()
    q = deque()
    cal = len(T) - len(S)
    q.append(T)

    for _ in range(cal):
        q_len = len(q)
        for _ in range(q_len):
            now = q.popleft()
            remove_char(now)

    flag = False
    while q:
        if q.popleft() == S:
            flag = True
            break
    if flag:
        print(1)
    else:
        print(0)