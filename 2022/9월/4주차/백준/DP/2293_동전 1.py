n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)    #dp는 동전의 합이 해당 인덱스의 숫자가 되는 경우의 수를 저장함
dp[0] = 1 #하나의 동전으로만 k원을 채우는 경우의 수 1가지

for coin in coins:  #모든 동전에 대해
    for num in range(coin, k+1):    #가장 작은 동전의 1개 가격부터 k원까지
        dp[num] += dp[num-coin]     #dp에는 해당 동전이 더해지기 전의 dp (num-coin) 값이 더해진다

print(dp[k])

