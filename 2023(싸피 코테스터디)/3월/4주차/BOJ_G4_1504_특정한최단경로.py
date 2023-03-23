import sys
from collections import defaultdict
from heapq import *

input = sys.stdin.readline

N, E = map(int, input().split())
graph = defaultdict(list)
for i in range(E):
    s, e, c = map(int, input().split())
    graph[s].append([c,e])
    graph[e].append([c,s])
# print(graph)
toGo1, toGo2 = list(map(int, input().split()))
INF = int(1e9)


def dijkstra(start):
    dis = [INF] * (N + 1)
    dis[start] = 0
    q = []
    heappush(q,[0,start])   # cost기준 heappush
    while q:
        now_cost ,now = heappop(q)
        if now_cost > dis[now]:
            continue
        for next in graph[now]:
            next_cost = now_cost + next[0]
            if next_cost < dis[next[1]]:
                dis[next[1]] = next_cost
                heappush(q,[next_cost, next[1]])
    # print(dis)
    return dis

dis_1 = dijkstra(1)     #1 ->
dis_toGo1 = dijkstra(toGo1)     #toGo1 ->
dis_toGo2 = dijkstra(toGo2)     #toGo2 ->

res = INF
res = min(dis_1[toGo1] + dis_toGo1[toGo2] + dis_toGo2[N], dis_1[toGo2] + dis_toGo2[toGo1] + dis_toGo1[N])

if res >= INF:
    print(-1)
else:
    print(res)