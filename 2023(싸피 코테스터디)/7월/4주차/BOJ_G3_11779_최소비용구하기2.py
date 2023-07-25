import sys, heapq

input = sys.stdin.readline
INF = 1e9

def dijkstra(start, end):

    city = [(0, start)]
    distance[start] = 0


    while city:
        now_cost, now_vertex  = heapq.heappop(city)
        if distance[now_vertex] < now_cost:
            continue
        for next in graph[now_vertex]:
            next_cost, next_vertex = next
            if distance[next_vertex] > now_cost + next_cost:
                distance[next_vertex] = now_cost + next_cost
                prev[next_vertex] = now_vertex
                if next_vertex != end:
                    heapq.heappush(city, (distance[next_vertex], next_vertex ))


if __name__ == '__main__':
    n = int(input())
    m = int(input())


    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append((c,e)) # 도착 지점, 비용

    start, end = map(int, input().split())
    prev = [-1] * (n + 1)
    distance = [INF] * (n + 1)
    dijkstra(start, end)
    # print(distance)
    path = [end]

    cur = end
    while prev[cur] != start:
        path.append(prev[cur])
        cur = prev[cur]

    path.append(start)
    # print(prev)
    print(distance[end])
    print(len(path))
    print(*path[::-1])