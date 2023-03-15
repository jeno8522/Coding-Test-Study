import sys

input = sys.stdin.readline

n = int(input())
q = []
tmp = list(map(int, input().split()))
for i in range(n):
    q.append(tmp[i])

res = []
arr = [i + 1 for i in range(n)]
start = 0

res.append(arr.pop(start))
move = q.pop(start)

while q:
    if move > 0:
        start = (start + move -1) % len(arr)
        move = q.pop(start)
        res.append(arr.pop(start))

    else:
        start = (start + move) % len(arr)
        move = q.pop(start)
        res.append(arr.pop(start))


print(*res)