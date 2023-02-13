n = int(input())
pdjs = [0]
for _ in range(n):
    pdj = int(input())
    pdjs.append(pdj)

dp = [0]    #해당 포도주를 마시고 바로 전 포도주를 마실때 전 전 전 dp값을 참조해야 하는데 dp 최신화하려면 i가 3부터 시작하므로 0을 넣고 시작
dp.append(pdjs[1])  #dp의 의미는 해당 순서까지의 포도주의 최댓값
if n > 1:
    dp.append(pdjs[1] + pdjs[2])

for i in range(3, n + 1):
    max_dp = max(dp[i-1], pdjs[i] + pdjs[i-1] + dp[i-3], pdjs[i] + dp[i-2])
    dp.append(max_dp)
print(dp[n])