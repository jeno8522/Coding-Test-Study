import sys

input = sys.stdin.readline


def cal():
    dp[1][0][0], dp[1][1][1] = 1, 1
    dp[2][0][0], dp[2][0][1], dp[2][1][1] = 2, 1, 1
    dp[3][0][0], dp[3][1][0], dp[3][0][1], dp[3][1][1], dp[3][2][1] =  3, 1, 2, 1, 1
    for i in range(4, 101):
        for j in range(i-1):
            dp[i][j][0] += (dp[i-1][j][0] + dp[i-1][j][1])
        for j in range(i-2):
            dp[i][j][1] += (dp[i-2][j][0]+ dp[i-2][j][1])
        for j in range(i-1):
            dp[i][j+1][1] += dp[i-1][j][1]



if __name__ == '__main__':
    T = int(input())
    arr = [list(map(int, input().rstrip().split())) for _ in range(T)]
    dp = [[[0] * 2 for _ in range(101)] for _ in range(101)] # 이차원 배열로 푸려고 하니 전 단계의 1로 시작하는 부분 > 1로시작하는 부분을 못구하더라
    cal()
    # for i in range(1,10):
    #     print(dp[i])
    for line in arr:
        n, k = line
        print(sum(dp[n][k]))