from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)      #해당 인덱스에 이어진 도시 저장

def bfs(start: int):
    shortcuts = []
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1   #visit 처리
                q.append(next)      #다음 도시들을 q에 삽입
                distance[next] = distance[now] + 1  #현재 도시의 거리에 + 1을 next에 삽입
                if distance[next] == k:     #경로 중에 최단 거리가 한번이라도 있으면 최단 경로에 삽입
                    shortcuts.append(next)
    if len(shortcuts) == 0:
        print(-1)
    else:
        shortcuts.sort()
        for city in shortcuts:
            print(city)

bfs(x)