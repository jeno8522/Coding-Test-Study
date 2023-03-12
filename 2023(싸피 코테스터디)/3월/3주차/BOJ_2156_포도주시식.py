import sys

input = sys.stdin.readline

n = int(input())
wines = [0]
dp = [0]*(n+1)

for i in range(n):
    wine = int(input())
    wines.append(wine)

for i in range(1, n + 1):
    if i < 3:
        dp[i] = wines[i] + dp[i-1]
    else:
        dp[i] = max(dp[i-1], wines[i] + dp[i-2], wines[i] + wines[i-1] + dp[i-3] )
        # 현재 포도주를 안마시거나, 현재 포도주와 전전 포도주의 최적해를 마시거나, 현재 포도주와 전 포도주와 전전전 포도주의 최적의 해 중 최댓값
        # 현재 포도주와 전 포도주의 최적해를 마실 순 없음( 전 포도주의 최적해가 몇 번 연속 마셨는 지 알 수 없으므로)
print(dp[n])


# dp는 해당 인덱스까지 선택할 수 있는 최적의 해
