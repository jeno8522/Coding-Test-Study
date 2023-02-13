n, m = map(int, input().split())
arr = list(map(int, input().split()))

res = -1
tmp = 0
isFinished = False
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            res = max(res, arr[i] + arr[j] + arr[k])
print(res)