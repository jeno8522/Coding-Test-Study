from typing import *

n,m,v = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    start_v, end_v = map(int, input().split())
    graph[start_v].append(end_v)
    graph[end_v].append(start_v)

for i in range(len(graph)):
    graph[i].sort()

def bfs(start_index: int) -> list[int]:
    queue = [start_index]
    discovered = [start_index]

    while queue:
        v = queue.pop(0)    #큐에 저장된 인덱스 pop
        for w in graph[v]:  #해당 인덱스인 정점에 연결된 정점들을 순회
            if w not in discovered:
                discovered.append(w)    #방문 정점을 저장
                queue.append(w)     #큐에 해당 인덱스인 정점에 연결된 정점들을 저장 (방문 예정인 정점들)
    return discovered

def dfs(start_index: int, discovered = []) -> list[int]:
    discovered.append(start_index)  # 방문한 정점을 추가 (a)
    for w in graph[start_index]:    #방문한 정점에 연결된 정점 순회
        if w not in discovered:
            discovered = dfs(w, discovered)  #방문한 적이 없으면 그 정점에 대해 dfs 호출 -> (a)에 의해 dfs에 의한 순서로 정점이 누적, 저장됨
    return discovered   # 모든 정점을 돌고나면 리턴


print(*dfs(v))
print(*bfs(v))