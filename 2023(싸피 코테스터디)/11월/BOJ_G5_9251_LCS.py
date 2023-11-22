import sys


input = sys.stdin.readline



if __name__ == '__main__':
    fir = input().rstrip()
    sec = input().rstrip()

    f_len, s_len = len(fir), len(sec)

    dp = [0] * s_len

    for i in range(f_len):
        max_val = 0
        for j in range(s_len):
            if dp[j] > max_val:
                max_val = dp[j]
            elif fir[i] == sec[j]:
                dp[j] = max_val + 1
    print(max(dp))