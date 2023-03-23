import heapq
import sys
from heapq import *

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    res = 0
    while len(files) > 1:
        file1 = heapq.heappop(files)
        file2 = heapq.heappop(files)
        res += file1 + file2
        heapq.heappush(files, file1 + file2)
    print(res)