import sys

input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(key=lambda x: (x[0], x[1]))

now_start = 0
now_end = sys.maxsize
result = 1
for meeting in info:
    start, end = meeting[0], meeting[1]
    if start < now_end:
        if end <= now_end:
            now_start = start
            now_end = end
    else:
        now_start = start
        now_end = end
        result += 1
print(result)

