import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N+1)]  # dp 값은 해당 원소까지 사용하여 해당 무게 인덱스로 창출할 수 있는 최대 가치
info = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,N+1):
    w, v = info[i-1][0], info[i-1][1]
    # if i == 1 and w <= K and v > 0:
    #     dp[i][w] = v
    #     continue
    for j in range(1, K + 1):
        if j < w:   # w보다 작은 무게의 index는 전의 dp 값 그대로 삽입
            dp[i][j] = dp[i-1][j]
        else:   # w와 같거나 큰 무게의 index의 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)    # 전 원소의 dp 값, 현재 원소의 가치 + 현재 원소의 무게 만큼 뺀 전 원소의 dp 값 중 최댓값으로 갱신

print(dp[-1][-1])
