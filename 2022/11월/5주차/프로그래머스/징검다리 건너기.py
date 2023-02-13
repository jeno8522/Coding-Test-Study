def solution(stones, k):
    l, r = 1, 200000000
    while l <= r:
        # print(l, r)
        mid = (l + r) // 2
        cnt = 0
        for s in stones:
            if s - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            r = mid - 1
        else:
            l = mid + 1
    return l

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))