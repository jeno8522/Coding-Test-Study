from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = [input().rstrip() for _ in range(n+m)]
counter = Counter(info)
result = 0
for e in counter.values():
    if e == 2:
        result += 1
print(result)
tmp = counter.most_common(result)
tmp.sort(key=lambda x:x[0])
for e in tmp:
    print(e[0])