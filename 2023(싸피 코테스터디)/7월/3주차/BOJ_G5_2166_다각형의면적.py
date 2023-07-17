import sys, math

input = sys.stdin.readline


def cal_width(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2


if __name__ == '__main__':
    n = int(input())
    width = 0

    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, input().split()))

    for i in range(n - 1):
        x1, y1 = graph[i]
        x2, y2 = graph[i + 1]
        width += cal_width(x1, y1, x2, y2)
    width += cal_width(graph[-1][0], graph[-1][1], graph[0][0], graph[0][1])

    print(round(abs(width), 1)/2)
