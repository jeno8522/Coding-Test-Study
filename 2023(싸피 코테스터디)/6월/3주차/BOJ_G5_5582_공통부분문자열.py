import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()
f = len(first)
s = len(second)
dp = [[0 for _ in range(s)] for _ in range(f)]
result = 0
for i in range(f):
    for j in range(s):
        if first[i] == second[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            result = max(result, dp[i][j])
print(result)