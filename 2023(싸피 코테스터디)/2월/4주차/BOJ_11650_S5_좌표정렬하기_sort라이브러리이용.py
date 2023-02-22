import sys
input = sys.stdin.readline

N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]

dots = sorted(dots, key= lambda x : (x[0], x[1]))
for dot in dots:
    print(dot[0], dot[1])