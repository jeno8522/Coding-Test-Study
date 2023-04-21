
def dfs(r, c, p, cnt):
    global res
    if cnt == N:
        res += p
        return

    graph[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        np = p * per[i]
        if graph[nr][nc] == 1:
            continue
        dfs(nr,nc,np,cnt+1)
        graph[nr][nc] = 0
    # return

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, e, w, s, n = map(int, input().split())
per = [e / 100,w / 100,s / 100,n / 100]
graph = [[0] * 29 for _ in range(29)]
# graph[14][14] = 1
res = 0
dfs(14,14,1,0)
print(float(res))