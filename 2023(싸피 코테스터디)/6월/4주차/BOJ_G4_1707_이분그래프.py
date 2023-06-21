import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, True))     # 1번 정점부터 탐색 시작

    visited[start] = True       # 1번 정점은 True 처리
    while q:
        now, flag = q.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = not flag
                q.append((next, visited[next]))
            elif visited[next] == flag:
                return False
    return True
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V+1)]
        for _ in range(E):
            s, e = map(int, input().split())
            graph[s].append(e)
            graph[e].append(s)
        visited = [-1] * (V + 1)  # 해당 정점의 flag 저장

        result = True
        for i in range(1, V+1):
            if visited[i] == -1:
                if not bfs(i):
                    result = False
                    break
        if result:
            print('YES')
        else:
            print('NO')