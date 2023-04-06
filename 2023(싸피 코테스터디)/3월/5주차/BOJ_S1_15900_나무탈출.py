import sys
from collections import deque

input = sys.stdin.readline


def bfs(): #  leaf 노드를 제외한 internal 노드의 개수를 bfs 방식으로 찾기
    global total
    q = deque()
    q.append((1, 0))
    visited[1] = 1
    while q:
        now, w = q.popleft()
        visited[now] = 1
        isLeaf = True    # 자식이 있는지 없는지의 정보를 저장하는 flag
        for next in graph[now]:
            if visited[next]: # 이미 방문했으면 continue
                continue
            isLeaf = False  # 자식이 하나라도 존재하면 leaf노드 아님
            visited[next] = 1 # 방문 체크
            q.append((next, w + 1)) # q에 next, w + 1 넣기
        if isLeaf: # leaf 노드면 해당 경로의 internal 갯수 total에 합산
            total += w


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
total = 0
for _ in range(n - 1): # 트리의 정보 양방향 저장
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# bfs 호출 하여 leaf 노드를 제외한 internal  ]노드의 개수 구하기
bfs()
# print(total)
if total % 2 == 1: #  leaf 노드를 제외한 internal  노드의 개수가 홀수면 이김
    print("Yes")
else:              # 짝수면 짐
    print("No")

# O(NlogN)이 아닐까?
