import sys

input = sys.stdin.readline

if __name__ == '__main__':
    fir = input().rstrip()
    sec = input().rstrip()

    len_f, len_s = len(fir), len(sec)

    dp = [[0] * (len_s + 1) for _ in range(len_f + 1)]

    max_value = -1
    for i in range(1, len_f + 1):
        for j in range(1, len_s + 1):
            if fir[i - 1] == sec[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            max_value = max(max_value, dp[i][j])
    print(max_value)
