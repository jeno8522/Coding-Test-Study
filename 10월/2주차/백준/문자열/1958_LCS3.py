# from itertools import combinations
# str1 = input()
# str2 = input()
# str3 = input()
#
# max = 0
# for i in range(len(str1), 1, -1):
#     if i > len(str2) or i > len(str3):
#         continue
#     isFinished = False
#     for per in combinations(str1, i):
#         if ''.join(per) in str2 and ''.join(per) in str3:
#             max = i
#             isFinished = True
#     if isFinished:
#         break
# print(max)

str1 = input()
str2 = input()
str3 = input()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

dp = [[[0]*(len3+1) for _ in range(len2+1)] for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        for k in range(1,len3+1):
            if str1[i-1] == str2[j-1] and str2[j-1] == str3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

res = -1

for i in range(len1+1):
    for j in range(len2+1):
        res = max(max(dp[i][j]), res)
print(res)