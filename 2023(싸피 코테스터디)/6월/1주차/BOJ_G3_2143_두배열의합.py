import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in range(1, n):
    a[i] += a[i-1]
# print(a)
for i in range(1, m):
    b[i] += b[i-1]

A = a[:]
for combi in combinations(a, 2):
    A.append(combi[1] - combi[0])
B = b[:]
for combi in combinations(b, 2):
    B.append(combi[1] - combi[0])

AC = Counter(A)
result = 0
for e in B:
    result += AC[t-e]
print(result)
