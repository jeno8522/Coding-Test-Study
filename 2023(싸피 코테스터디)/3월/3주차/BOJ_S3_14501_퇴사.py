import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)  # 해당 지점까지 창출할 수 있는 가치의 최댓값

for i in range(N):
    p, v = info[i][0], info[i][1]
    for j in range(i + p, N + 1):   # 현재 상담 이후 일정 (남은 퇴사일을 넘을 경우 그냥 넘어가짐)
        dp[j] = max(dp[j], dp[i] + v)   # 기존 저장된 가치와 현재 상담 이전 가치 + 현재 상담의 가치 의 최댓값 갱신
print(dp[-1])

# 0   1   2   3   4   5   6   7
# 0   0   0   0   0   0   0   0
# 0   0   0   0   10  10  10  10
# 0   0   0   0   10  10  10   20
# 0   0   0   0   10  10  10  30
# 0   0   0   0   10  10  10  45




