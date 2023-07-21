import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def findSet(v):
    if parent[v] == v:
        return v
    parent[v] = findSet(parent[v])
    return parent[v]


if __name__ == '__main__':
    g = int(input())
    p = int(input())
    planes = [int(input()) for _ in range(p)]

    parent = [0] * (g+1)
    for i in range(g+1):
        parent[i] = i

    result = 0
    for e in planes:
        k = findSet(e)
        if k == 0:
            break
        parent[k] = k - 1
        result += 1
    print(result)