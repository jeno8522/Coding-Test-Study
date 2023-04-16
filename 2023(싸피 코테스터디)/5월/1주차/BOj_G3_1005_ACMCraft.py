import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    dp = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    deg = [0] * (N+1)       # 차수
    for i in range(K):
        s, e = map(int, input().split())
        graph[s].append(e)
        deg[e] += 1
    q = deque() # 차수가 0인 건물
    for i in range(1, N+1):
        if deg[i] == 0:
            q.append(i)
            dp[i] += time[i]
            deg[i] -= 1

    while q:
        now = q.popleft()
        deg[now] -= 1
        for next in graph[now]:
            dp[next] = max(dp[next], dp[now] + time[next])
            deg[next] -= 1
            if deg[next] == 0:
                q.append(next)

    W = int(input())
    print(dp[W])
