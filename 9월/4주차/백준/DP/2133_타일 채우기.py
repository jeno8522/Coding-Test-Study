n = int(input())        #타일링 문제는 무한대로 직접 세어보면서 규칙을 찾아서 점화식 작성하기
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4,n+1) :
    if i%2 == 0 :
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else :
        dp[i] = 0
print(dp[n])