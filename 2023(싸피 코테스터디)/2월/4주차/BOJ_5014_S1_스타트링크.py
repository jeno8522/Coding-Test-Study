import sys
from collections import deque

input = sys.stdin.readline


def bfs(cnt):
    q = deque()
    q.append((S, cnt))
    while q:
        now, now_cnt = q.popleft()
        if now == G:
            return now_cnt
        up = now + U
        down = now - D
        if down >= 1:
            if not visited[down]:
                visited[down] = 1
                q.append((down, now_cnt + 1))
        if up <= F:
            if not visited[up]:
                visited[up] = 1
                q.append((up, now_cnt + 1))
    return -1


F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)
res = bfs(0)
if res == -1:
    print("use the stairs")
else:
    print(res)