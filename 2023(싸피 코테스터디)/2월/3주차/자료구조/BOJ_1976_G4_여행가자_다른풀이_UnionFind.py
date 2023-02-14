import sys


def find(v):
    if v == g[v]:
        return v
    else:       #경로 압축
        g[v] = find(g[v])
        return g[v]
    # else:     일반적인 방법
    #     return find(g[v])



def merge(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return

    g[v] = u


N = int(input())
M = int(input())

g = [0] * N
for i in range(N):
    g[i] = i

for i in range(N):
    v = list(map(int, input().split()))
    for j in range(N):
        if v[j] == 1:
            merge(i, j)  # union

v = list(map(int, input().split()))
v[:] = [x - 1 for x in v]
for i in range(M):
    if find(v[0]) != find(v[i]):
        print("NO")
        exit()
print("YES")
