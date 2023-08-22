import sys


input = sys.stdin.readline


def make_parents():
    for i in range(1, n+1):
        parents[i] = i

def find(v):
    while v != parents[v]:
        v = parents[v]
    return v


def union(v, u):
    pv, pu = find(v), find(u)
    if pv > pu:
        parents[pv] = parents[pu]
    else:
        parents[pu] = parents[pv]


if __name__ == '__main__':
    n, m = map(int, input().split())
    parents = [0] * (n+1)
    make_parents()

    result = 0
    isFinished = False
    for i in range(m):
        s, e = map(int, input().split())
        if find(s) == find(e) and not isFinished:
            result = i + 1
            isFinished = True

        union(s, e)

    print(result)

