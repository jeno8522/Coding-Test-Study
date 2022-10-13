import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def make_graph():
    for e in graph_info:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

def bfs(num: int):
    visited[num] = 1
    for e in graph[num]:
        if not visited[e]:
            bfs(e)

n, m = map(int, input().split())
graph_info = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

make_graph()
for i in range(1, len(graph)):
    if not visited[i]:
        if not graph[i]:
            visited[i] = 1
            cnt += 1
        else:
            bfs(i)
            cnt += 1

print(cnt)