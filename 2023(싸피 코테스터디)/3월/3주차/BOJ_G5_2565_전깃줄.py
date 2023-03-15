import sys

input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info = sorted(info)

dp = [0] * n    #dp 값은 해당 인덱스까지의 가장 긴 증가하는 부분수열의 값
for i in range(n):
    for j in range(i):
        if info[i][1] > info[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
# print(dp)
print(n - max(dp))





# 시작 지점이 작다면 끝 지점도 작아야함
# 시작 지점이 크다면 끝 지점도 커야함
# 정렬 ?
# dp 값이 의미하는 바는? 해당 전깃줄까지 이을 수 있는 전깃줄의 최적 값 (최댓값)?
# 500번까지, 100개의 전깃줄
# 제거할 전깃줄 최솟값 => 연결할 전깃줄 최댓값
# 전 요소보다 시작 포인트가 커지니깐 끝나는 포인트가 더 커져야함
# 시작 포인트 기준 정렬 -> 끝나는 포인트 가장 긴 증가하는 부분수열