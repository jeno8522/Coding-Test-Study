import sys
from collections import deque

input = sys.stdin.readline


def findDiameter(root):
    l = r = 0
    visited = [0] * (n + 1)
    q = deque()
    visited[root] = 1

    # root의 왼쪽 길이 구하기
    q.append((graph[root][0][0], graph[root][0][1]))
    visited[graph[root][0][0]] = 1
    while q:
        now, now_w = q.popleft()
        l = max(l, now_w)
        for e in graph[now]:
            next, next_w = e[0], e[1]
            if visited[next]:
                continue
            visited[next] = 1
            q.append((next, now_w + next_w))

    # root의 오른쪽 길이 구하기
    if len(graph[root]) > 1:
        q = deque()
        q.append((graph[root][1][0], graph[root][1][1]))
        visited[graph[root][1][0]] = 1
        while q:
            now, now_w = q.popleft()
            r = max(r, now_w)
            for e in graph[now]:
                next, next_w = e[0], e[1]
                if visited[next]:
                    continue
                visited[next] = 1
                q.append((next, now_w + next_w))
    return l + r  # 구한 지름 return


n = int(input())
graph = [[] for _ in range(n + 1)]
if n == 1:
    print(0)
    exit(0)

for _ in range(n - 1):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])

ans = 0

for i in range(1, n + 1):
    ans = max(ans, findDiameter(i))
print(ans)
