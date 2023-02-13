from typing import *

n = int(input())
a = list(map(int, input().split()))
# a = [map(int, input().split())]  이거 오류남
dp = [0 for _ in range(n)]

def dp_sequence() -> int:
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j]:   #i가 j보다 값이 더크고 dp값은 작을때
                dp[i] = dp[j]                   #j의 dp값을 i의 dp에 대입
        dp[i] += 1                              #i의 dp값을 방문시에 +1
    return max(dp)

print(dp_sequence())