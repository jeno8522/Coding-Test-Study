from typing import *

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]   # R에 전 집의 G, B중 최솟값 + 자기 자신 저장
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]   # 위와 방식과 동일
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]   # 위의 방식과 동일

print(min(dp[n-1])) # 마지막 집에 쌓여있는 최솟값끼리 더한 정보 중 최솟값 출력