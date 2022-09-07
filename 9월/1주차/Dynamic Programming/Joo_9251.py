from typing import *

str1 = input()
str2 = input()
dp = [0 for _ in range(len(str2))]   #str2에 대한 cache

for i in range(len(str1)):
    cnt = 0
    for j in range(len(str2)):
        if cnt < dp[j]:     #누적값 체크 먼저, cache에 저장된 누적값이 cnt보다 크면 cnt에 저장
            cnt = dp[j]
        elif str1[i] == str2[j]:    #두 문자열에 같은 문자에 방문하면 그 전까지의 누적값 + 1을 cache에 저장
            dp[j] = cnt + 1

print(max(dp))  #저장된 누적값 중 max 값 출력