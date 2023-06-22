import sys
import heapq
input = sys.stdin.readline



if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e, v = map(int, input().split())
        graph[s].append((v, e))
        graph[e].append((v, s))

    hq = []
    hq.append((0,1))
    result = 0
    visited = [False] * (V+1)
    visited[1] = True
    while hq:
        v, now = heapq.heappop(hq)
        if not visited[now]:
            visited[now] = True
            result += v
        for next in graph[now]:
            if visited[next[1]]:
                continue
            heapq.heappush(hq, (next[0], next[1]))
        # print(v)
    print(result)
    # print(visited)