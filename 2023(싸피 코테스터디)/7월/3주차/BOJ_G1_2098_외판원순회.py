import sys

input = sys.stdin.readline

INF = 1e9

def dfs(start, visited):
    if visited == (1 << n) -1:
        if graph[start][0]:
            return graph[start][0]
        else:
            return INF

    if dp[start][visited] != INF:
        return dp[start][visited]


    for i in range(1, n):
        if not graph[start][i]:
            continue
        if visited & (1 << i):
            continue
        dp[start][visited] = min(dp[start][visited], dfs(i, visited|(1<<i)) + graph[start][i])
    return dp[start][visited]

if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        graph[i] = line
    dp = [[INF] * (1 << n) for _ in range(n)]
    print(dfs(0, 1))
