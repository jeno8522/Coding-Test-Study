from collections import deque, defaultdict


def bfs(num):
    q = deque()
    visited = defaultdict(int)
    q.append((num, 0))
    visited[num] = 1
    while q:
        now, cnt = q.popleft()
        # print(now, cnt)
        if now == A:
            return cnt + 1
        if now % 2 == 0 and visited[now // 2] != 1 and now // 2 > 0:
            visited[now // 2] = 1
            q.append((now // 2, cnt + 1))
        if now % 10 == 1 and visited[now // 10] != 1 and now // 10 > 0:
            visited[now // 10] = 1
            q.append((now // 10, cnt + 1))
    return -1


A, B = map(int, input().split())
time = 0
print(bfs(B))
