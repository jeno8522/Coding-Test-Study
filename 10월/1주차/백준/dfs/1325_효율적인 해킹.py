import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(num: int):
    visited.add(num)
    s.add(num)
    for e in graph[num]:
        if not e in visited:
            dfs(e)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
res = []
cnt_len = []

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
for i in range(1, n+1):
    visited = set()
    s = set()
    dfs(i)
    cnt_len.append(len(s))
max_len = max(cnt_len)
for i in range(n):
    if cnt_len[i] == max_len:
        print(str(i+1) + ' ', end="")
