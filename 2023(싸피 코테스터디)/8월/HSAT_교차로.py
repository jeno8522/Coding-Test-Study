import sys

input = sys.stdin.readline


def indexing(c):
    if c == 'A' or c == 'C':
        return 0
    else:
        return 1


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n)]
    a, b, c, d = [], [], [], []
    result = [-1] * n

    for i in range(n):
        time, char = input().strip().split()
        graph[i] = [int(time), char]

    graph.sort(key=lambda x : x[0])

    a.sort(key=lambda x: x[0])
    b.sort(key=lambda x: x[0])
    c.sort(key=lambda x: x[0])
    d.sort(key=lambda x: x[0])

    cnt, time = 0, 0
    a_idx, b_idx, c_idx, d_idx = 0, 0, 0, 0
    while True:

