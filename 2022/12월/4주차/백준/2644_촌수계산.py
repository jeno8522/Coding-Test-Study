def dfs(start, cnt):
    if start == target:
        res.append(cnt)
    if graph[start] and not visited[start]:
        visited[start] = 1
        # print(visited)
        for e in graph[start]:
            dfs(e, cnt + 1)


n = int(input())
start, target = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
res = []
for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

dfs(start, 0)
if not res:
    print(-1)
else:
    print(res[0])

