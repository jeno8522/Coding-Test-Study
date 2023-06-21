import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, 0
sum = arr[0]
min_len = sys.maxsize
while True:
    if sum >= s:
        min_len = min(min_len, r-l+1)
        sum -= arr[l]
        l += 1
    else:
        r += 1
        if r == n:
            break
        sum += arr[r]
if min_len == sys.maxsize:
    min_len = 0
print(min_len)