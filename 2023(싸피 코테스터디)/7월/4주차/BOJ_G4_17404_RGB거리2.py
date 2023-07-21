import sys

input = sys.stdin.readline
INF = 1e9


if __name__ == '__main__':
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    minValue = sys.maxsize
    for i in range(3):
        dp = [[INF, INF, INF] for _ in range(n)]
        dp[0][i] = graph[0][i]
        tmp = sys.maxsize
        for j in range(1, n-1):
            dp[j][0] = graph[j][0] + min(dp[j-1][1], dp[j-1][2])
            dp[j][1] = graph[j][1] + min(dp[j-1][0], dp[j-1][2])
            dp[j][2] = graph[j][2] + min(dp[j-1][0], dp[j-1][1])

        for j in range(3):
            if i != j:
                dp[-1][j] = graph[-1][j] + min(dp[n-2][(j+1)%3], dp[n-2][(j-1)%3])
        tmp = min(dp[-1])
        minValue = min(minValue, tmp)
    print(minValue)