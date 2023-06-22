import sys
input = sys.stdin.readline

def make_parents():
    for i in range(1, V+1):
        parents[i] = i

def find(v):
    if v == parents[v]:
        return v
    parents[v] = find(parents[v])
    return parents[v]

def union(v, u):
    parents[find(v)] = parents[find(u)]

if __name__ == '__main__':
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    parents = [-1] * (V+1)

    info = sorted(info, key= lambda x: x[2])
    make_parents()
    result = 0

    for line in info:
        if find(line[0]) != find(line[1]):
            result += line[2]
            union(line[0], line[1])

    print(result)