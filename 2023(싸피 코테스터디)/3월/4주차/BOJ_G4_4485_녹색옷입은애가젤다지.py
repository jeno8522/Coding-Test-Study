import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
dr = [1, 0, 0, -1]
dc = [0, 1, -1, 0]

tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    dis = [[INF] * n for _ in range(n)]
    dis[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (dis[0][0], 0, 0))
    while q:
        w, r, c = heapq.heappop(q)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if dis[r][c] < w:
                continue

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            cost = w + graph[nr][nc]
            if cost >= dis[nr][nc]:
                continue
            dis[nr][nc] = cost
            heapq.heappush(q, (cost, nr, nc))

    print("Problem {}: {}".format(tc, dis[-1][-1]))
    tc += 1
