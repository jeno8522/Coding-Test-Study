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

    goal = len(S)
    result = -1
    while True:
        # print(T)
        if len(T) == goal:
            if T == S:
                result = 1
            else:
                result = 0
            break
        if T[-1] == 'A':
            T = T[:-1]
        else:
            T = T[:-1]
            T = T[::-1]

    print(result)