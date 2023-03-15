import sys
input = sys.stdin.readline

n = int(input())
graph = [int(input()) for _ in range(n)]

dp = [0] * n
for i in range(n):
    for j in range(i):
        if graph[i] > graph[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))