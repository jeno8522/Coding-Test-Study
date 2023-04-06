import sys
from collections import deque

input = sys.stdin.readline


def findDiameter(root): # root를 기준으로
    l = r = 0   # 왼쪽 자식의 길이 구하기
    visited = [0] * (n + 1)
    q = deque()
    visited[root] = 1

    # root의 왼쪽 길이 구하기 - BFS
    q.append((graph[root][0][0], graph[root][0][1]))
    visited[graph[root][0][0]] = 1
    while q:
        now, now_w = q.popleft()
        l = max(l, now_w) # 왼쪽 길이의 최댓값 갱신
        for e in graph[now]: # 전 노드에 연결된 자식들을 검사
            next, next_w = e[0], e[1]
            if visited[next]: # 방문 체크
                continue
            visited[next] = 1
            q.append((next, now_w + next_w)) # 전 노드까지의 가중치에 현 노드의 가중치 더해서 q에 넣어줌

    # root의 오른쪽 길이 구하기 - 위와 동일
    if len(graph[root]) > 1:
        q = deque()
        q.append((graph[root][1][0], graph[root][1][1]))
        visited[graph[root][1][0]] = 1
        while q:
            now, now_w = q.popleft()
            r = max(r, now_w)
            for e in graph[now]:
                next, next_w = e[0], e[1]
                if visited[next]:
                    continue
                visited[next] = 1
                q.append((next, now_w + next_w))
    return l + r  # 구한 지름 return


n = int(input())
graph = [[] for _ in range(n + 1)]
if n == 1: # 노드가 하나일 경우 지름은 0
    print(0)
    exit(0)

for _ in range(n - 1): # 트리의 정보 양방향으로 저장
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])

ans = 0

for i in range(1, n + 1): # 전체 노드를 순회하면서 해당 노드를 root로 하는 트리의 지름 최댓값 갱신
    ans = max(ans, findDiameter(i))
print(ans)

#O(NlogN) 이지 않을까?
