import sys

input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())

    max_dp = [[0,0,0] for _ in range(n+1)]
    min_dp = [[0,0,0] for _ in range(n+1)]

    arr = list(map(int, input().split()))
    max_dp[1] = arr
    min_dp[1] = arr

    for i in range(2, n+1):
        arr = list(map(int, input().split()))
        max_dp[i][0] = max(max_dp[i-1][0] + arr[0] , max_dp[i-1][1] + arr[0])
        max_dp[i][1] = max(max_dp[i-1][0] + arr[1], max_dp[i-1][1] + arr[1], max_dp[i-1][2] + arr[1])
        max_dp[i][2] = max(max_dp[i-1][1] + arr[2], max_dp[i-1][2] + arr[2])

        min_dp[i][0] = min(min_dp[i-1][0] + arr[0] , min_dp[i-1][1] + arr[0])
        min_dp[i][1] = min(min_dp[i-1][0] + arr[1], min_dp[i-1][1] + arr[1], min_dp[i-1][2] + arr[1])
        min_dp[i][2] = min(min_dp[i-1][1] + arr[2], min_dp[i-1][2] + arr[2])

    print(max(max_dp[n]), min(min_dp[n]))