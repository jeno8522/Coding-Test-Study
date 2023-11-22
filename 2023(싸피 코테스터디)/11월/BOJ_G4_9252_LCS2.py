import sys


input = sys.stdin.readline



if __name__ == '__main__':
    fir = input().rstrip()
    sec = input().rstrip()

    f_len, s_len = len(fir), len(sec)

    dp = [[0] * (s_len+1) for _ in range(f_len+1)]
    res = ''

    for i in range(1,f_len+1):
        max_val = 0
        for j in range(1,s_len+1):

            if max_val < dp[i][j]:
                max_val = dp[i][j]

            elif fir[i-1] == sec[j-1]:
                max_val += 1
                dp[i][j] = max_val
            else:
                dp[i][j] = max_val
    max_val = 0
    for i in range(1, f_len+1):
        if max_val < dp[i][-1]:
            max_val = dp[i][j]
            res += fir[i-1]
    print(dp[-1][-1])
    print(res)

    print(*dp, sep='\n')