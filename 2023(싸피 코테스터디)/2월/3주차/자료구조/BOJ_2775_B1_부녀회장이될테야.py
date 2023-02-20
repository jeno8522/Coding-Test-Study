T = int(input())
for _ in range(T):
    res = 0
    K = int(input())
    N = int(input())
    arr = [i for i in range(N + 1)]
    for i in range(K):
        res = 0
        for j in range(1, N+1):
            res += arr[j]
            arr[j] = res
    print(res)




