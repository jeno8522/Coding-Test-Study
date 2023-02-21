import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input().rstrip()) for _ in range(K)]

left, right = 1, max(lines)


answer = 0
mid = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)

#
# 4 11
#
# 1 802 401 5
# 1 400 200 11
# 201 400 300 6
# 201 299 249 8
# 201 248 224 9
# 201 223
