n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(n-1):
    dp.append(max(dp[i]+arr[i+1], arr[i+1]))    #dp는 해당 인덱스 까지의 최댓값, 해당 인덱스 까지의 최댓값 + 다음 값 or 다음 값 중 큰 값으로 dp 최신화
print(max(dp))