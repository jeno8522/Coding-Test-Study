n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(k + 1):
    dp[0][i] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
print(dp[-1][-1] % 1000000000)

# [0 선택, N을 k-1개로 만들기], [1, N-1을 k-1개로]...[N-1, 1을 k-1개로], [N, 0을 k-1개로]
# dp[N][K] = dp[0][k-1] + dp[1][k-1] ... dp[n-1][k-1] + dp[n][k-1]
# = dp[n-1][k] + dp[n][k-1]
