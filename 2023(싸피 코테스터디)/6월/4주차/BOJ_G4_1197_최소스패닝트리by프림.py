import sys
import heapq
input = sys.stdin.readline


#프림 알고리즘
if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e, v = map(int, input().split())
        graph[s].append((v, e))
        graph[e].append((v, s))

    hq = []
    hq.append((0,1))    # 첫 탐색 스타트 위치 (가중치는 0, 1번 정점)
    result = 0
    visited = [False] * (V+1)   # 정점 방문 체크
    # visited[1] = True
    while hq:
        v, now = heapq.heappop(hq)  # 힙으로 가중치가 가장 작은 다음 정점 pop
        if visited[now]:    # 해당 정점이 앞에서 더 작은 가중치로 이미 방문(연결) 되어 있음 -> continue
            continue
        visited[now] = True # 이번 정점 방문(연결) 처리, 가중치 더해줌
        result += v
        for next in graph[now]: # 이번 정점에 연결된 다음 정점 힙에 넣어줌
            if visited[next[1]]:    # 다음 정점이 이미 연결되어 있다면 continue
                continue
            heapq.heappush(hq, (next[0], next[1]))
        # print(v)
    print(result)
    # print(visited)