
import sys
sys.stdin = open("input.txt", "r")

for t in range(int(input())):
    n,k = map(int,input().split())
    dp = [[0] * (k+1) for _ in range(n+1)]
    items = [list(map(int,input().split())) for _ in range(n)]
    # print(items)

    for i in range(1,n+1):
        for j in range(1,k+1):  #부피
            if items[i - 1][0] <= j:    #인덱스 0 부피, 인덱스 1 가치 , 같은 갯수인 인덱스에서 하나 덜쓴 같은 부피
                dp[i][j] = max(dp[i - 1][j], items[i - 1][1] + dp[i - 1][j - items[i - 1][0]])  #하나 더쓴 디피는  하나 덜쓴 같은부피, 하나 덜쓴 이번 꺼랑 하나덜쓴 전체에서 이번꺼 뺀거
            else:
                dp[i][j] = dp[i - 1][j]
            # print(dp)
    print(f'#{t+1} {dp[n][k]}')

    dp = [[0] * (K + 1) for _ in range(N + 1)]
    # 부피, 가치
    for i in range(1, N + 1):
        v, c = items[i - 1]
        for j in range(1, K + 1):
            if v > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - v] + c, dp[i - 1][j])