import sys
from collections import deque
input = sys.stdin.readline

def bfs(): # 1번 노드에서 가장 멀리 떨어진 노드까지의 길이 구하기
    global max_dis
    q = deque()
    q.append((1,0)) # 1번 방부터 시작하므로 1번부터 bfs 시작
    visited[1] = 1  # 1번 노드 방문 체크
    while q:
        now, now_w = q.popleft()
        for e in graph[now]:
            next, next_w = e[0], e[1]
            if visited[next]:
                continue
            visited[next] = 1  # 방문 체크
            max_dis = max(max_dis, now_w + next_w) # 전 노드까지의 길이에 현 노드의 가중치를 더해 최댓값 갱신
            q.append((next, now_w + next_w)) # 해당 정보 q에 넣어줌



n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
max_dis = 0
for _ in range(n-1): # 트리 정보 양방향 저장
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

bfs()
print(max_dis)

# O(N) 아닐까?
