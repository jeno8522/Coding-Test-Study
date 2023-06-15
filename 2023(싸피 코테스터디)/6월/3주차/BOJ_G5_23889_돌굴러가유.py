import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
castle = list(map(int, input().split()))
rock = list(map(int, input().split()))
collapse = {}

for i in range(n - 2, -1, -1):
    castle[i] += castle[i + 1]
# print(castle)
for i in range(k - 1):
    collapse[rock[i]] = castle[rock[i] - 1] - castle[rock[i + 1] - 1]
collapse[rock[k - 1]] = castle[rock[k - 1] - 1]
# print(collapse)
collapse = sorted(collapse.items(), key=lambda x: x[1], reverse=True)
# print(collapse)
collapse = sorted(collapse[:m], key=lambda x:x[0])
for e in collapse:
    print(e[0])
