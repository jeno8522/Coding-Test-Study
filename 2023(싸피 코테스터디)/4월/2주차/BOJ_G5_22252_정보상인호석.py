import sys
from heapq import *
from collections import defaultdict

input = sys.stdin.readline

Q = int(input())
info = defaultdict(list)
res = 0

for _ in range(Q):
    line = list(input().split())
    cmd, name, k = line[0], line[1], int(line[2])
    if cmd == '1':
        values = list(map(int, line[3:]))
        for val in values:
            heappush(info[name], - val)
    else:
        for _ in range(k):
            if not info[name]:
                break
            res += - heappop(info[name])
print(res)