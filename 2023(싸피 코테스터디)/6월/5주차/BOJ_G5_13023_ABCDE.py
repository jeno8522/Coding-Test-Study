import sys

input = sys.stdin.readline

def dfs(now, cnt):
    if cnt == 4:
        return True
    visited[now] = True
    for next in graph[now]:
        if visited[next]:
            continue
        if dfs(next, cnt + 1):
            return True
    visited[now] = False
    return False
if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    result = 0
    for i in range(n):
        visited = [False] * n
        if dfs(i, 0):
            result = 1
            break
    print(result)