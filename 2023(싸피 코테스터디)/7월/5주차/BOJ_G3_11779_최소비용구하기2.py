import sys, heapq
input = sys.stdin.readline
INF = 1e9
def dijkstra(start, end):
    distance = [INF] * (n+1)
    # visited = [False]
    distance[start] = 0
    city = [(start,0)]

    while city:
        now, now_v = heapq.heappop(city)
        for next in graph[now]:
            # print(next)
            e, next_v = next
            # print(e, v)
            if distance[e] < next_v:
                continue
            distance[e] = min(distance[e], now_v+next_v)
            route.add(e)
            heapq.heappush(city, (e, next_v))
    print("city = ", distance)
    print("route = ", route)


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, v = map(int, input().split())
        # print(s, e, v)
        graph[s].append((e,v))
    # print(graph)
    route = set()
    start, end = map(int, input().split())
    dijkstra(start, end)
