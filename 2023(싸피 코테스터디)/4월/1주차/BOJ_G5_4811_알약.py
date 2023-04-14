import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]  # i는 h, j는 w
for j in range(31):
    dp[0][j] = 1    # w로 알약이 세팅되어 있을 때 지금 먹는 경우의 수 1

for i in range(1, 31):  #h는 최소 1, 최대 n개
    for j in range(i, 31):  #w는 최소 h갯수 만큼 세팅 -> 끝까지
        dp[i][j] = dp[i-1][j] + dp[i][j-1]    # h를 i번 먹고 w를 j번 먹는 경우의 수 ==
                                              # h를 i-1번 w를 j번 먹고 h 먹기 + h를 i번 w를 j-1번 먹고 w먹기
while True:
    num = int(input())
    if num == 0:
        break
    print(dp[num][num])    # w n개, h n개 먹기