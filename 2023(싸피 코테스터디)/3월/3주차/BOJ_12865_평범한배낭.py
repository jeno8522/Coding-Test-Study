import sys
input = sys.stdin.readline

n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0]]]
for i in range(1, n+1):
    if i == 1:
        dp.append([[info[i-1][0], info[i-1][1]]])
        continue
    if info[i-1][0] > k or info[i-1][1] == 0:
        tmp = []
        for e in dp[i-1]:
            tmp.append(e)
        dp.append(tmp)
        continue
    tmp = [[info[i-1][0], info[i-1][1]]]
    for e in dp[i-1]:
        nw, nv = info[i - 1][0] + e[0], info[i - 1][1] + e[1]
        if nw > k:
            continue
        else:
            tmp.append([nw, nv])
    dp.append(tmp)

max_value = -1
for e in dp[-1]:
    if max_value < e[1]:
        max_value = e[1]
print(max_value)

