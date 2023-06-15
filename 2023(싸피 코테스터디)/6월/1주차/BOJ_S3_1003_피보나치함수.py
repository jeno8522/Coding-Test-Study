def fibonacci(n):
    global cnt0, cnt1
    if n == 0:
        cnt0 += 1
        return 0
    elif n == 1:
        cnt1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    T = int(input())
    orders = [int(input()) for _ in range(T)]
    max_val = max(orders)

    dp0 = [0] * (41)
    dp0[0] = 1
    dp1 = [0] * (41)
    dp1[1] = 1
    for i in range(2, 41):
        dp0[i] = dp0[i-2] + dp0[i-1]
        dp1[i] = dp1[i-2] + dp1[i-1]
    for e in orders:
        print(dp0[e], dp1[e])