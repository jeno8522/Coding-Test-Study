import sys

input = sys.stdin.readline




if __name__ == '__main__':
    n = int(input())
    dp = [0] + [1] * 9

    for i in range(n-1):
        copy = dp[:]
        dp[0] = copy[1]
        for j in range(1, 9):
            dp[j] = copy[j-1] + copy[j+1]
        dp[9] = copy[8]

    print(sum(dp) % 1000000000)